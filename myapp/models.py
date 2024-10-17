from django.db import models


class Profile(models.Model):
    emp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    status = models.CharField(max_length=100, default='active')
    role = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=15, null=True)
    emergency_contact = models.CharField(max_length=20, null=True)
    blood_group = models.CharField(max_length=5, null=True)
    nationality = models.CharField(max_length=50, null=True)
    religion = models.CharField(max_length=50, null=True)
    marital_status = models.CharField(max_length=10,null=True)
    address = models.TextField(null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.name}"




class BankInfo(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=20)
    pan_no = models.CharField(max_length=100)

    def __str__(self):
        return self.account_number
    


class Education(models.Model):
    institution_name = models.CharField(max_length=255)  
    degree = models.CharField(max_length=255) 
    start_year = models.IntegerField()   
    end_year = models.IntegerField()  

    def __str__(self):
        return self.institution_name    
    


class Experience(models.Model):
    title = models.CharField(max_length=255) 
    start_date = models.CharField(null=True)               
    end_date = models.CharField(null=True, blank=True) 
    duration = models.TextField(null=True) 

    def __str__(self):
        return self.title
    
    
   

