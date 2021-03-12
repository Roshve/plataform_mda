from django.db import models

# Create your models here.


class Leader(models.Model):
    #model of new user
    
    #Model Leader
    leader_email = models.EmailField(max_length=320, blank=True)

    leader_name = models.CharField(max_length=100, blank=True)

    leader_lastname = models.CharField(max_length=100, blank=True)

    cost_center = models.IntegerField()

    product =  models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class NewUser(models.Model):
    #Model New Employee

    leader = models.ForeignKey(Leader, null=True, on_delete=models.CASCADE)

    employee_name = models.CharField(max_length=100, blank=True)

    employee_lastname = models.CharField(max_length=100, blank=True)

    management_consulting = models.CharField( max_length=100, blank=True)

    employee_dni = models.IntegerField()

    profile_equal = models.CharField(max_length=100, blank=True)

    employee_replace = models.CharField(max_length=100, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
