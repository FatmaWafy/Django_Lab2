from django.db import models
 

class School(models.Model):
    name = models.CharField(max_length=255)
    number_of_classes = models.IntegerField()
    area = models.FloatField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    area = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.school.name})"

