# -*- coding: utf8 -*-
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import TestModel


class IndexView(TemplateView):
    template_name = 'index.html'


class UsersList110(TemplateView):
    template_name = 'users_list_1_10.html'


class UsersList110Json(BaseDatatableView):
    model = User


class TestModelList(TemplateView):
    template_name = 'testmodel_list.html'


class TestModelListJson(BaseDatatableView):
    model = TestModel
    # columns and order columns are provided by datatables in the request using "data" in columns definition


# backward compatibility with Datatables 1.9.x
class UsersList(TemplateView):
    template_name = 'users_list.html'


class UsersListJson(BaseDatatableView):
    model = User
    columns = ['username', 'email']
    order_columns = ['username', 'email']

    def filter_queryset(self, qs):
        sSearch = self.request.GET.get('sSearch', None)
        if sSearch:
            qs = qs.filter(Q(username__istartswith=sSearch) | Q(email__istartswith=sSearch))
        return qs
