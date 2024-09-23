from django.urls import path

from users.api.views import getUsersView

urlpatterns = [
    path("users/", getUsersView.as_view()),
]