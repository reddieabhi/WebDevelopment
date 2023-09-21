from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField(default=20)
    email = models.EmailField()
    
    place = models.CharField(max_length=40)
    file = models.FileField()




class Car(models.Model):
    c_name = models.CharField(max_length=40)
    speed = models.IntegerField(default=60)


    def __str__(self) -> str:
        return self.c_name
    
