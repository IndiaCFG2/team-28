from django.db import models
import datetime
from django.contrib.postgres.fields import ArrayField

class FPO(models.Model):
	fid=models.CharField(max_length=200, default='',primary_key=True)
	statename=models.CharField(max_length=200, default='')
	district=models.CharField(max_length=200, default='')
	programme=models.CharField(max_length=200, default='')
	resource=models.CharField(max_length=200, default='')
	name=models.CharField(max_length=200, default='')
	legalformfpo=models.CharField(max_length=200, default='')
	registration_date=  models.DateField( default=datetime.date.today)
	address=models.CharField(max_length=300, default='')
	crops=ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
	contact=models.CharField(max_length=300, default='')

	def __str__(self):
		return self.name



class ForumComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.TextField(default="Anonymous")
    fpo = models.ForeignKey(FPO,null=True,on_delete=models.CASCADE,blank=True,to_field="fid")
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,to_field="sno")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment




class fpoproduct(models.Model):
	pid=models.AutoField(primary_key=True)
	productname=models.CharField(max_length=200, default='')
	fponame=models.CharField(max_length=200, default='')
	description=models.CharField(max_length=200, default='')
	timeline= models.DateField( default=datetime.date.today)
	quantity=models.CharField(max_length=200, default='')
	price=models.IntegerField(default=0)
	fpo= models.ForeignKey(FPO, on_delete=models.CASCADE,to_field="fid")

	def __str__(self):
		return self.fponame
