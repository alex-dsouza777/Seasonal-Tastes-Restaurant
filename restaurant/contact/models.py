from django.db import models

# Create your models here.
class Feedback(models.Model):
    subject = models.CharField(max_length=100)
    from_email = models.EmailField(max_length=100)
    message = models.TextField()