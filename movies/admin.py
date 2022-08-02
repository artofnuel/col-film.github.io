from django.contrib import admin
from .models import Movie, MovieComment, School, UserInfo
# from .forms import CustomSignupForm

# admin.site.register(CustomSignupForm)

# Register your models here.
admin.site.register(Movie)
admin.site.register(MovieComment)
admin.site.register(School)
admin.site.register(UserInfo)
