from django.db import models


class Profile(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, default='active')
    role = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=5)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=10)
    address = models.TextField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"



