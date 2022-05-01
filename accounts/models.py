from django.db import models

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.username

class CategoryTable(models.Model):
    category_name = models.CharField(max_length=20)


    def __str__(self):
        return self.category_name

class DoctorsTable(models.Model):

    dr_category = models.ForeignKey(CategoryTable, on_delete= models.CASCADE)
    dr_name = models.CharField(max_length=80)
    dr_img = models.ImageField(upload_to='pics')
    dr_qualification = models.CharField(max_length=40)
    dr_address = models.CharField(max_length=254)
    dr_city = models.CharField(max_length=30)
    dr_email = models.EmailField(max_length=254)
    dr_mobile = models.TextField()
    
    def __str__(self):
        return self.dr_name


class AppointMail(models.Model):
    dr_detail = models.ForeignKey(DoctorsTable, on_delete= models.CASCADE)
    patient_name = models.CharField(max_length=60)
    appoint_date = models.DateField(auto_now=False)
    appoint_time = models.TimeField(auto_now=False)

    def __str__(self):
        return self.patient_name