# from django.db import models

# # Create your models here.
# class ForumComment(models.Model):
#     sno = models.AutoField(primary_key=True)
#     comment = models.TextField()
#     user = models.TextField(default="Anonymous")
#     #include fpo model
#     fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.comment




# class fpoproduct(models.Model):
# 	pid=models.AutoField(primary_key=True)
# 	productname=models.CharField(max_length=200, default='')
# 	fponame=models.CharField(max_length=200, default='')
# 	description=models.CharField(max_length=200, default='')
# 	timeline=models.DateField(default=date.today)
# 	quantity=models.CharField(max_length=200, default='')
# 	price=models.IntegerField(default=0)
# 	fid= models.ForeignKey(FPO, on_delete=models.CASCADE)



# class FPO(models.Model):
# 	fid=models.CharField(max_length=200, default='')
# 	statename=models.CharField(max_length=200, default='')
# 	district=models.CharField(max_length=200, default='')
# 	programme=models.CharField(max_length=200, default='')
# 	resource=models.CharField(max_length=200, default='')
# 	name=models.CharField(max_length=200, default='')
# 	legalformfpo=models.CharField(max_length=200, default='')
# 	date= models.DateField( default=date.today)
# 	address=models.CharField(max_length=300, default='')
# 	crops=models.ListCharField(
#         base_field=CharField(max_length=10),
#         size=6,
#         max_length=(6 * 11)  
#     )
# 	contact=models.CharField(max_length=300, default='')


