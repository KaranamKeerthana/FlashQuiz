from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    word=models.CharField(max_length=3000,blank=True)
    meaning=models.CharField(max_length=3000,blank=True)
    example=models.CharField(max_length=3000,blank=True)
    mnemonic=models.CharField(max_length=3000,blank=True)


    

    def __str__(self):
        return self.word
