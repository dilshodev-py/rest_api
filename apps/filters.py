from django_filters import FilterSet, NumberFilter

from apps.models import Category


class CategoryFilterSet(FilterSet):

    class Meta:
        model = Category
        fields = 'id','name'