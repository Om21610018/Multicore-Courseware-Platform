from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content_type_choices = [
        ('LAB', 'Lab'),
        ('QUIZ', 'Quiz'),
        ('ASSESSMENT', 'Assessment'),
        ('BLOG', 'Blog'),
    ]
    content_type = models.CharField(max_length=20, choices=content_type_choices)
    content = models.TextField()
    sequence_no = models.IntegerField()

    def __str__(self):
        return f"{self.content_type} - {self.title}"
    
class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class UserCourseContentProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_content = models.ForeignKey(CourseContent, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.course_content.title}"

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
    
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_issued = models.DateField(auto_now_add=True)
    # Add more fields as needed, such as certificate template, etc.

    def __str__(self):
        return f"Certificate of Completion for {self.course.title} - {self.user.username}"
    
