from django.urls import path

from . import views


app_name = "forbidden_app"
urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "users/",
        views.UserListView.as_view(),
        name="user-list",
    ),
    path(
        "403/",
        views.ForbiddenView.as_view(),
        name="403",
    ),
]
