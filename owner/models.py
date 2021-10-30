from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse



class Owner(models.Model):
    # A way to keep track of current settings
    name = models.CharField(max_length=250)
    key = models.IntegerField(default=0, unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    '''
    http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    '''
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         + "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    # Owner can put whatever dates they want
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    )
    OpenFromWD = models.CharField(max_length=10, choices=DAY_CHOICES)
    OpenUntilWD = models.CharField(max_length=10, choices=DAY_CHOICES)
    OpenSaturday = models.BooleanField(default=1)
    OpenSunday = models.BooleanField(default=0)
    SundayStart = models.TimeField()
    SundayEnd = models.TimeField()
    SaturdayStart = models.TimeField()
    SaturdayEnd = models.TimeField()
    WeekdayStart = models.TimeField()
    WeekdayEnd = models.TimeField()

    # Any notes the owner would like to add
    Notes = models.CharField(max_length=250,blank=True, null=True)

    def get_absolute_url(self):
        return reverse('owner:index')

    def __str__(self):
        return self.name
