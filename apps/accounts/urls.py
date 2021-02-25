from django.urls import path

from .views import (
    LoginAPIView, SignUpAPIView, ActivateAPIView, LogoutAPIView,
    ResendActivationEmailAPIView, ProfileAPIView, ChangePasswordAPIView,
    ResetPasswordAPIView, ResetPasswordConfirmAPIView, UserWithoutTeamAPIView
)

urlpatterns = [
    path('login', view=LoginAPIView.as_view(), name='login'),
    path('signup', view=SignUpAPIView.as_view(), name='signup'),
    path('activate/<slug:eid>/<slug:token>', view=ActivateAPIView.as_view(),
         name='activate'),
    path('logout', view=LogoutAPIView.as_view(), name='logout'),
    path('resend-activation-link', view=ResendActivationEmailAPIView.as_view(),
         name='resend'),
    path('profile', view=ProfileAPIView.as_view(), name='profile'),
    path('password/change', ChangePasswordAPIView.as_view()),
    path('password/reset', view=ResetPasswordAPIView.as_view(),
         name='reset password'),
    path('password/reset/confirm', view=ResetPasswordConfirmAPIView.as_view(),
         name='confirm password'),
    path('without_team', view=UserWithoutTeamAPIView.as_view(), name='users_without_team')
]
