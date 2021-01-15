from django.db import models
from django.contrib.auth.models import User

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
    zip_code = models.IntegerField(null=True)
    email = models.EmailField()
    mobile = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " " + self.state

class ServiceStatus(models.Model):
    serial_no = models.AutoField(primary_key=True)
    service_id = models.IntegerField()
    status_description = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Request Id: " + str(self.service_id) + " - " + self.status_description[0:10] + "...."
    
class AssignTechnician(models.Model):
    serial_no = models.AutoField(primary_key=True)
    request_id = models.IntegerField(null=True)
    request_info = models.CharField(max_length=100)
    description = models.TextField()
    name = models.CharField(max_length=25)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.IntegerField(null=True)
    email = models.EmailField()
    mobile = models.IntegerField()
    technician = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + " " + self.state

class TechnicianList(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    joining_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.employee_id) + " - " + self.name + " - " + self.email

class UserProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="dashboard/")

    def __str__(self):
        return str(self.user) + " " + "Profile Picture"

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_details = models.ForeignKey(UserProfilePicture, on_delete=models.CASCADE, null=True)
    review_title = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return "self.user_details.user.first_name"
    


