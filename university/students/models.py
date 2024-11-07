from django.db import models

class Profile(models.Model):
    phone_num = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.phone_num} {self.address}"
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Course(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Professor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name="professors")

    def __str__(self):
        return f"Professor {self.name} {self.surname}"
    
class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="classes")

    def __str__(self):
        return f"Class for {self.course.title}"


