from django.shortcuts import render
from django_api_github.views import RecordList,RecordDetail

# Create your views here.
def index(request):
    records=RecordList()
    queryset=records.get_queryset()
    context={"Record_list" : queryset}
    return render(request, 'index.html', context=context)
def record_detail(request,repository_ID):
    record = RecordDetail(request=request).get_queryset()[0]

    context = {'record': record}
    print(record.get_all_fields())
    return render(request, 'detail.html', context=context)