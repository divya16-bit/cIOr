from django.contrib import admin


from .models import CustomUser, UserOTP, User, record
admin.site.register(UserOTP)
admin.site.register(record)
admin.site.register(User)
admin.site.register(CustomUser)

