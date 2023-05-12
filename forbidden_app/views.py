from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


def index(request):
    return render(request, "forbidden_app/index.html")


# class UserListView(ListView, UserPassesTestMixin):  # Remember to inherit UserPassesTestMixin before ListView
class UserListView(UserPassesTestMixin, ListView):
    """
    View for listing users.
    """

    model = User
    template_name = "forbidden_app/user_list.html"
    context_object_name = "users"

    def test_func(self):
        """
        Return `True` if the User is not an `AnonymouUser`.
        """
        return not isinstance(self.request.user, AnonymousUser)


class ForbiddenView(TemplateView):
    """
    View for 403 Forbidden errors.
    """

    template_name = "forbidden_app/403.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "You are not authorized to view this page."
        return context
