from django.db import models

# Create your models here.

class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    message = models.TextField()

    def __str__(self):
        return self.name + " " + "-" + " " + self.email
    