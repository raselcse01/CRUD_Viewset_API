from django.db import models

# Create your models here.

STUDENT_CLASS  =(
    ("One", "One"),
    ("Two", "Two"),
    ("Three", "Three"),
    ("Four", "Four"),
    ("Five", "Five"),
)

GENDER = [
    ('Male'  , 'Male'  ),
    ('Female', 'Female'),
]

class Student(models.Model):
    name          = models.CharField(max_length = 100, null=True, blank=True)
    student_class = models.CharField(choices=STUDENT_CLASS, max_length=20)
    gender        = models.CharField(choices=GENDER, max_length=20)

    roll          = models.IntegerField(null=True, blank=True)
    email         = models.EmailField(max_length=50, unique=True)
    

    waiver        = models.BooleanField(default=False)

    date_of_birth = models.DateField()
    created_at    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name