from django.db import models

class Account(models.Model):
   email_id = models.CharField(max_length=100,blank=True,null=True)
   account_name = models.CharField(max_length=10,blank=True,null=True)
   App_secret_token = models.CharField(max_length=10,blank=True,null=True)

class  Destination(models.Model):
   account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
   urls = models.URLField(max_length=100,blank=True,null=True)
   http_method = models.CharField(max_length=100,blank=True,null=True)
   headers = models.CharField(max_length=100,blank=True,null=True)

   def __str__(self):
        return self.urls

# Create your models here.
