from django.db import models
from django.utils.timezone import now


class Company(models.Model):

    class CompanyStatus(models.TextChoices):
        LAYOFFS = 'Layoffs'
        HIRING_FREEZE = 'Hiring Freeze'
        HIRING = 'Hiring'

    name = models.CharField(max_length=20, unique=True)
    status = models.CharField(choices=CompanyStatus.choices, max_length=20, default=CompanyStatus.HIRING)
    url = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(default=now, editable=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
