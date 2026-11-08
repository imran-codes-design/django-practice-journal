from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    pub_date=models.DateTimeField("date published")

    def __str__(self):
        return self.name