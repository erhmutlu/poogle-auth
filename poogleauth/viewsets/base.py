from rest_framework import mixins, viewsets, filters

__author__ = 'erhmutlu'


class OrderedListModelMixin(mixins.ListModelMixin):
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class BaseModelWithPaginationViewSet(viewsets.ModelViewSet, OrderedListModelMixin):
    _ignore_view_permissions = True
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = OrderedListModelMixin.filter_backends + (filters.SearchFilter,)

    class Meta:
        abstract = True