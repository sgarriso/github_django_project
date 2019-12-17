from rest_framework import serializers  # @UnresolvedImport
from github_display_app.models import GithubRecord
class GithubRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GithubRecord
        fields = '__all__'
        