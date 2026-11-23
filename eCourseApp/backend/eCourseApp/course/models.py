from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PROTECT


class User(AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null= True)
    update_date = models.DateTimeField(auto_now=True, null =True)

    class Meta:
        abstract = True

class Category (BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course (BaseModel):
    subject = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course/%Y/%M')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject
    class Meta:
        unique_together = ('subject', 'category')

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='lesson/%Y/%M')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name