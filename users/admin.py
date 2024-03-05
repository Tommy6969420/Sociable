from django.contrib import admin
from.models import User, Response, Post, ResposePost,UserImage
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['full_name','username','contact_email']
    search_fields=['full_name','username','contact_email']
class PostAdmin(admin.ModelAdmin):
    list_display=['author']
    list_filter=['upload_time','author',]
    search_fields=['author','description']
admin.site.register(Response)
admin.site.register(ResposePost)
admin.site.register(User,UserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(UserImage)