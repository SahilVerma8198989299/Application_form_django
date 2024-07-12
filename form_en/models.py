from django.db import models

# Create your models here.

# Create your models here.
class form_enquirys(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    job_role=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=30)
    pincode=models.IntegerField()
    # datee=models.DateField()
    def __str__(self):
        return self.full_name
    