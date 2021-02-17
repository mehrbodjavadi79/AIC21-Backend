from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from apps.ticket import paginations
from .models import Ticket, Reply
from .serializers import TicketSerializer, ReplySerializer
from .services import SendTicketToTelegramChannel


class TicketAPIView(GenericAPIView):
    serializer_class = TicketSerializer

    def get(self, request, ticket_id):
        ticket = get_object_or_404(Ticket, id=ticket_id)
        data = self.get_serializer(instance=ticket).data

        return Response(
            data={'data': data},
            status=status.HTTP_200_OK
        )


class UserTicketsListAPIView(GenericAPIView):
    serializer_class = TicketSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()

        send_ticket_to_telegram = SendTicketToTelegramChannel(ticket=ticket)
        send_ticket_to_telegram.run()

        return Response(
            data={"detail": "Your ticket has been submitted"},
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        tickets = Ticket.objects.filter(author=request.user)
        data = self.get_serializer(instance=tickets, many=True).data

        return Response(
            data={'data': data},
            status=status.HTTP_200_OK
        )


class PublicTicketsListAPIView(GenericAPIView):
    serializer_class = TicketSerializer

    def get(self, request):
        tickets = Ticket.objects.filter(is_public=True)
        data = self.get_serializer(instance=tickets, many=True).data
        return Response(
            data={'data': data},
            status=status.HTTP_200_OK
        )


class ReplyListAPIView(GenericAPIView):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all().order_by('-created')
    pagination_class = paginations.ReplyPagination

    def get(self, request, ticket_id):
        replies = self.get_queryset().filter(ticket__id=ticket_id)
        data = ReplySerializer(replies, many=True).data
        return Response(data)

    def post(self, request, ticket_id):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ticket_id=ticket_id)
        return Response({"detail": "Your Reply has been submitted"})
