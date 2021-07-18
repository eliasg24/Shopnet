# Django
from django.urls import path

# Vistas
from users.views import UserListView, UserAddView, UserDetailView, delete_user

urlpatterns = [
    path(
        route="list/",
        view=UserListView.as_view(),
        name="list"
    ),
    path(
        route="add/",
        view=UserAddView.as_view(),
        name="add"
    ),
    path(
        route="<int:pk>/",
        view=UserDetailView.as_view(),
        name="detail"
    ),
    path(
        route="delete/",
        view=delete_user,
        name="delete"
    )
]
