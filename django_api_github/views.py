from rest_framework import generics  # @UnresolvedImport
from github_display_app.models import GithubRecord 
from .serializer import GithubRecordSerializer
from .permissions import RecordPermissions
class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GithubRecord.objects.all()
    serializer_class = GithubRecordSerializer
    permission_classes = (RecordPermissions,)
    lookup_field = 'repository_ID'
class RecordList(generics.ListCreateAPIView):
    serializer_class = GithubRecordSerializer
    permission_classes = (RecordPermissions,)
  
    def get_queryset(self):
        #serializer = BreatherSerializer(data=self.request.data)
        #serializer.is_valid(raise_exception=True)
        
        return GithubRecord.objects.all()