from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from .models import Vagas
from .filters import VagasFilter


def index(request):
    vagas_list=Vagas.objects.all ().order_by ('-register_date')
    vagas_filter=VagasFilter (request.GET, queryset=vagas_list)
    paginator=Paginator (vagas_filter.qs, 10)
    page=request.GET.get ('page')
    paginas = paginator.get_page(page)



    template_name='vagas/index.html'
    context={
        'vagas': vagas_list,
        'filter': vagas_filter,
        'paginas': paginas,

    }
    return render (request, template_name, context)
