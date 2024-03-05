from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES=(
        ("male","male"),
        ('female',"female"),
    ('others',"others"),)
    username=models.CharField(max_length=20,unique=True,null=False,blank=False)
    password=models.CharField(max_length=20,null=False,blank=False)
    full_name=models.CharField(max_length=20,null=False,blank=False)
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,default="male")
    contact_email=models.EmailField()
    contact_number=models.CharField(max_length=15,blank=False,null=False)
    date_of_birth=models.DateField()
    def __str__(self):
        return f"{self.full_name} {self.username}"

class Response(models.Model):
    responder=models.ForeignKey(User,on_delete=models.CASCADE)
    # post=models.ForeignKey(Post,on_delete=models.CASCADE)
    like_count=models.IntegerField(default=0,blank=True,null=True)
    comment=models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.responder.username}"


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    description=models.TextField(blank=True,null=True)
    upload_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='status/',blank=True,null=True)
    # reactions=models.ManyToManyField(Response,null=True,blank=True)
    def __str__(self):
        return f"{self.author.username} {self.description}"
class ResposePost(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    response=models.ForeignKey(Response ,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.post.author} {self.response.responder}"
class UserImage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    image=models.ImageField(upload_to='profiles/',null=True,blank=True, default='profiles/avatar.jpg')
    def __str__(self):
        return f'{self.user}'