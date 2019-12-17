from django.contrib import admin

# Register your models here.
from .models import GithubRecord
admin.site.register(GithubRecord)