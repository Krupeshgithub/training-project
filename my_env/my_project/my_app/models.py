from django.db import models

# Create your models here.

class subject(models.Model):
    subject_name = models.CharField(max_length=50)
    total_marks = models.IntegerField()
    
    def __str__(self) -> str:
        return self.subject_name
    
class teacher(models.Model):
    teacher_name = models.CharField(max_length=50)    
    
    def __str__(self) -> str:
        return self.teacher_name
    
class student(models.Model):
    student_name = models.CharField(max_length=50)  
    roll_no  = models.IntegerField()
    Teacher = models.ForeignKey("teacher",on_delete=models.CASCADE)
    Subject = models.ForeignKey("subject",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.student_name
 
            