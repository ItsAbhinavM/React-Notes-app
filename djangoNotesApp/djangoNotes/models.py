from django.db import models

# Create your models here.
class Note(models.Model):
    noteText=models.CharField(max_length=255)
    date=models.DateField(auto_now_add=True)

    def __Str__(self):
        return self.title
    
