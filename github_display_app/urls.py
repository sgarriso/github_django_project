from django.urls import path

from . import views
app_name = 'github_display_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('record/<str:repository_ID>/', views.record_detail, name='record_detail'),
    
]
