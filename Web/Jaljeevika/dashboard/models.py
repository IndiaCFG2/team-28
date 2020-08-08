from django.db import models

# Create your models here.
class ForumComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.TextField(default="Anonymous")
    #include fpo model
    fpo = models.ForeignKey(FPO, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment