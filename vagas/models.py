from django.db import models
from taggit.managers import TaggableManager


class Vagas (models.Model):
    reference_number=models.BigIntegerField (blank=True, null=True)
    id=models.TextField (primary_key=True, blank=True, null=False)
    url=models.TextField (blank=True, null=True)
    title=models.TextField (blank=True, null=True)
    description=models.TextField (blank=True, null=True)
    register_date=models.TextField (blank=True, null=True)
    open_days=models.BigIntegerField (blank=True, null=True)
    quantity=models.BigIntegerField (blank=True, null=True)
    job_type=models.TextField (blank=True, null=True)
    study=models.IntegerField (blank=True, null=True)
    education=models.TextField (blank=True, null=True)
    work_time=models.TextField (blank=True, null=True)
    salary=models.TextField (blank=True, null=True)
    salary_type=models.TextField (blank=True, null=True)
    workplace=models.TextField (blank=True, null=True)
    country=models.TextField (blank=True, null=True)
    city=models.TextField (blank=True, null=True)
    state=models.IntegerField (blank=True, null=True)
    picker=models.TextField (blank=True, null=True)

    class Meta:
        managed=True
        db_table='vagas'

    def __str__(self):
        return self.title
