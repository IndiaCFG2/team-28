from django.contrib import admin
from .models import ForumComment,FPO,fpoproduct
# Register your models here.
admin.site.register(ForumComment)
admin.site.register(FPO)
admin.site.register(fpoproduct)