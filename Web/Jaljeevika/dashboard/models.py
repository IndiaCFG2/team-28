from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class FPO(models.Model):
	fid=models.CharField(primary_key=True,max_length=200, default='')
	statename=models.CharField(max_length=200, default='')
	district=models.CharField(max_length=200, default='')
	programme=models.CharField(max_length=200, default='')
	resource=models.CharField(max_length=200, default='')
	fponame=models.CharField(max_length=200, default='')
	legalformfpo=models.CharField(max_length=200, default='')
	registration_date=  models.DateField( default=datetime.date.today)
	address=models.TextField()
	crops=models.CharField(max_length=300, default='')
	contact=models.CharField(max_length=300, default='')



class ForumComment(models.Model):
    comment = models.TextField()
    user = models.TextField(default="Anonymous")
    #include fpo model
    FPO = models.ForeignKey(FPO, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,default='fid')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment




class fpoproduct(models.Model):
	productname=models.CharField(max_length=200, default='')
	fponame=models.CharField(max_length=200, default='')
	description=models.TextField()
	timeline= models.DateField( default=datetime.date.today)
	quantity=models.CharField(max_length=200, default='')
	res=models.FileField(upload_to='res_folder', blank=True)
	price=models.IntegerField(default=0)
	FPO= models.ForeignKey(FPO, on_delete=models.CASCADE,default='fid')
	created = models.DateTimeField(auto_now_add=True)