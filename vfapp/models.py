from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='profilepics',null=True ,blank=True)





class Posts(models.Model):

    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    caption=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images',null=True,blank=True)
    video=models.ImageField(upload_to="videos",null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    like=models.ManyToManyField(MyUser,related_name='like')


    def __str__(self):
        return self.description

class Comments(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    User=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)


