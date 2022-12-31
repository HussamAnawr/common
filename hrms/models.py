from django.db import models


class Employee(models.Model):
    MALE = 'M'
    FEMALE = 'FM'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'FEMALE'),
    ]
    MARRIED = 'MR'
    SINGLE = 'SG'
    STATUS = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
    ]
    RESIDENCE = 'RS'
    NATIONAL = 'ID'
    PASSPORT = 'PS'
    ID_TYPES = [
        (RESIDENCE, 'Residence No.'),
        (NATIONAL, 'National ID'),
        (PASSPORT, 'Passport No.')
    ]

    first_name = models.CharField(
        max_length=100, help_text='Enter first name.')
    middle_name1 = models.CharField(max_length=100, blank=True, null=True)
    middle_name2 = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, help_text='Enter last name.')
    id_type = models.CharField(
        max_length=2, choices=ID_TYPES, default=NATIONAL)
    national_id = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GENDERS, default=MALE)
    date_of_birth = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS, default=SINGLE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    pass


class Attendance(models.Model):
    pass


class Vacation(models.Model):
    REGULAR = 'RG'
    SICK = 'SK'
    MOTHERHOOD = 'MH'
    MATERNITY = 'MT'
    MARRIAGE = 'MG'
    DEATH = 'DT'
    EXAMS = 'EX'
    NEW_BORN = 'NB'
    TYPES = [
        (REGULAR, 'Regular Vacation'),
        (SICK, 'Sick Leave'),
        (MOTHERHOOD, 'Motherhood Vacation'),
        (MATERNITY, 'Maternity Leave'),
        (MARRIAGE, 'Marriage Leave'),
        (DEATH, 'Death Leave'),
        (EXAMS, 'Exams Leave'),
        (NEW_BORN, 'New Born Leave')
    ]
    type = models.CharField(max_length=2, choices=TYPES, default=REGULAR)
    start_date = models.DateField()
    period = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(
        'Employee', on_delete=models.CASCADE, related_name='vacations')
