import django_filters
from django_filters import DateFilter

from vagas.models import Vagas


class VagasFilter(django_filters.FilterSet):
    class Meta:
        model = Vagas
        fields = [
            'title', 'city','education', 'study', 'state']