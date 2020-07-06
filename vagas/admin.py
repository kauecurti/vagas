from django.contrib import admin

from .models import Vagas


class VagasAdmin (admin.ModelAdmin):
    list_display=['url', 'title', 'description', 'register_date', 'open_days',
                  'quantity', 'job_type', 'study', 'education',
                  'work_time', 'salary', 'salary_type', 'workplace', 'country',
                  'city', 'state', 'picker']

    search_fields=['title', 'register_date']
    prepopulated_fields={'register_date': ('title',)}


admin.site.register (Vagas, VagasAdmin)
# Register your models here.
