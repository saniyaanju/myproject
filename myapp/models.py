from django.db import models

# Create your models here
class Student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.IntegerField(default=1)
    dob=models.DateField(default=0)
    fees=models.IntegerField(null=True,blank=True,default=0)
    mobile=models.IntegerField(null=True,blank=True,default=0)
    cls=models.IntegerField(default=1)
class Meta:
    ordering = ['name']
    unique_toghethet=['name','rollno']

class Staff(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True,default=0)
    salary=models.IntegerField(null=True,blank=True,default=0)
    subject=models.CharField(max_length=50)
class Attendence(models.Model):
    student=models.ForeignKey(Student,related_name="studentattendence",on_delete=models.CASCADE)
    english=models.IntegerField(null=True,blank=True,default=0)
    hindi=models.IntegerField(null=True,blank=True,default=0)
    urdu=models.IntegerField(null=True,blank=True,default=0)
    physics=models.IntegerField(null=True,blank=True,default=0)
    maths=models.IntegerField(null=True,blank=True,default=0)
    chemistry=models.IntegerField(null=True,blank=True,default=0)
    biology=models.IntegerField(null=True,blank=True,default=0)
    computer=models.IntegerField(null=True,blank=True,default=0)
    
class Marks(models.Model):
    student=models.ForeignKey(Student,related_name="studentresult",on_delete=models.CASCADE)
    english=models.IntegerField(null=True,blank=True,default=0)
    hindi=models.IntegerField(null=True,blank=True,default=0)
    urdu=models.IntegerField(null=True,blank=True,default=0)
    physics=models.IntegerField(null=True,blank=True,default=0)
    maths=models.IntegerField(null=True,blank=True,default=0)
    chemistry=models.IntegerField(null=True,blank=True,default=0)
    biology=models.IntegerField(null=True,blank=True,default=0)
    computer=models.IntegerField(null=True,blank=True,default=0)
class Notice(models.Model):
    notice=models.TextField(null=True,blank=True,default=0)
class Notice2(models.Model):
    notice=models.TextField(null=True,blank=True,default=0)