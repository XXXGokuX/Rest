from django.db import models

# Create your models here.
class User(models.Model):
    email= models.EmailField(unique=True)
    username= models.CharField(max_length=255)
    password= models.CharField(max_length= 255)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'app_user'