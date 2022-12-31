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
    description = models.TextField(blank=True)
    responsibilities = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    section = models.ForeignKey(
        'Section', on_delete=models.CASCADE, related_name='jobs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['title',]

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Section(models.Model):
    TYPES = [
        ('DI', 'Directory'),
        ('MA', 'Management'),
        ('DE', 'Department'),
        ('TE', 'Team'),
    ]
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=TYPES, default='MA')
    parant = models.ForeignKey(
        'Section', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['title',]

    def __str__(self):
        return self.title
