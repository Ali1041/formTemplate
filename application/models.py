from django.db import models




# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=20)

    def __str__(self):
        return self.country_name


class Record(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=100, unique=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country')
    phone_number = models.IntegerField()
    birth_country = models.ForeignKey(Country,on_delete=models.CASCADE,related_name='birth_country')
    age = models.IntegerField()
    martial_status = models.CharField(max_length=128)
    speaking_english_level = models.CharField(max_length=128)
    education_level = models.CharField(max_length=128)
    been_to_canada = models.CharField(max_length=5)
    monthly_income = models.CharField(max_length=128)
    interested_visa = models.CharField(max_length=128)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class PaymentCharge(models.Model):
    user_record = models.ForeignKey(Record,on_delete=models.CASCADE,related_name='user_info')
    amount = models.FloatField(default=49.0)
    unit = models.CharField(max_length=10,default='USD')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_record.first_name} payed {self.amount} on {self.added_date}'