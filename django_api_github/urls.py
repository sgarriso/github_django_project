from django.urls import path,include
from .views import RecordList,RecordDetail



urlpatterns = [
    path('record/',RecordList.as_view()),
     path('record/<str:repository_ID>/', RecordDetail.as_view()),
    ]