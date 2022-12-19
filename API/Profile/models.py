from djongo import models

# Create your models here.

# Create your models here.
class ProfileDB(models.Model):
    _id=models.ObjectIdField()
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.EmailField(max_length=200 ,unique=True)
    password=models.CharField(max_length=200)
    # created_at=models.DateTimeField()
    
    

 