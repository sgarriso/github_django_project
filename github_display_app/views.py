from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)
def record_detail(request,repository_ID):
    return render(request, 'detail.html', context=None)