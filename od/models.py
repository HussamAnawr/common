from django.db import models


# Create your models here.


class Job(models.Model):
    SCHEDULES = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('ST', 'Shift')
    ]
    LEVELS = [
        ('SR', 'Senior'),
        ('MD', 'Middle'),
        ('JR', 'Junior'),
        ('GR', 'Graduate')
    ]
    reference_number = models.IntegerField
    title = models.CharField(max_length=255)
    schedule = models.CharField(max_length=2, choices=SCHEDULES, default='FT')
    level = models.CharField(max_length=2, choices=LEVELS, default='GR')

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
