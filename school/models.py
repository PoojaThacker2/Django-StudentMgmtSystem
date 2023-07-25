from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    students = models.ManyToManyField('Student', related_name='schools')


    def __str__(self):
        return self.name

class Student(models.Model):
    GRADE_CHOICES = [
        (1, 'Grade 1'), (2, 'Grade 2'), (3, 'Grade 3'), (4, 'Grade 4'),
        (5, 'Grade 5'), (6, 'Grade 6'), (7, 'Grade 7'), (8, 'Grade 8'),
        (9, 'Grade 9'), (10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12'),
    ]

    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    grade = models.PositiveSmallIntegerField(choices=GRADE_CHOICES)

    def __str__(self):
        return self.name
