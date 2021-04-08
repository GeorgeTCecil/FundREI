from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData["fname"]) < 2 or len(postData["lname"]) < 2:
            errors["name"] = "Both names must be at least 2 characters long."
        if len(postData["email"]) < 10:
            errors["email"] = "Invalid email address."
        if len(postData["password"]) < 8:
            errors["password"] = "Passwords must be at least 8 characters long."
        if postData["password"] != postData["conf_password"]:
            errors["password_match"] = "Passwords do not match!"
        return errors
    def project_validator(self, postData):
        errors={}
        if len(postData["title"]) < 3:
            errors["title"] = "Title must be at least three characters long."
        if len(postData["description"]) < 3:
            errors["description"] = "Description must be at least three characters long."
        if len(postData["location"]) < 3:
            errors["location"] = "Location must be at least three characters long."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
class Project(models.Model):
    creator = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    invested_by = models.ManyToManyField(User, related_name="invested_projects", blank=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=25, blank=True)
    roi = models.CharField(max_length=255, blank=True)
    units = models.CharField(max_length=25, blank=True)
    image = models.ImageField(upload_to='images/', default='', null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.title