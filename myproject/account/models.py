from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,email,first_name,password=None,user_type= 'normal_user'):
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,user_type=user_type)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self,email,first_name,password,user_type='admin'):
        user = self.model(email=email,first_name=first_name,user_type= user_type)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    user_type_choice = [
        ('normal_user', 'Normal User'),
        ('corporate_user', 'Corporate User'),
        ('admin', 'Admin')
    ]   

    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50,blank=True,null=True)
    user_type = models.CharField(max_length=50,choices=user_type_choice,default='normal_user')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = AccountManager()

    def __str__(self):
        return f'{self.email}({self.user_type})'
    
class Role(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length=50,unique=True)
    role = models.ForeignKey(Role,related_name='groups',on_delete=models.CASCADE,blank=True,null=True)


    def save(self,*args,**kwargs):
        if self.name == 'premium' and (not self.role or self.role.name != 'manager'):
            raise ValueError('Premium groups must be assigned to the Manager role')
        super().save(*args,**kwargs)
    





