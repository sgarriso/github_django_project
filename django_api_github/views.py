from rest_framework import generics  # @UnresolvedImport
from github_display_app.models import GithubRecord 
from .serializer import GithubRecordSerializer
from .permissions import RecordPermissions
class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = GithubRecordSerializer
    permission_classes = (RecordPermissions,)
    lookup_field = 'repository_ID'
    def get_queryset(self):
        queryset = GithubRecord.objects.all()
        
        #workspace = self.request.query_params.get('workspace')
        uri = self.request.get_full_path()
        repository_ID = uri.split('/')
        print(repository_ID)
        return queryset.filter(repository_ID=repository_ID[-2])
class RecordList(generics.ListCreateAPIView):
    serializer_class = GithubRecordSerializer
    permission_classes = (RecordPermissions,)
  
    def get_queryset(self):
        #serializer = BreatherSerializer(data=self.request.data)
        #serializer.is_valid(raise_exception=True)
        
        return GithubRecord.objects.all()