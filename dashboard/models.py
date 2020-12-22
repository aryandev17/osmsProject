from django.db import models

# Create your models here.

class SubmitRequest(models.Model):
    serial_no = models.AutoField(primary_key=True)
    request_info = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=25)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " " + self.state
    