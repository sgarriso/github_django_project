from rest_framework import permissions  # @UnresolvedImport
class RecordPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            return obj
    def has_permission(self, request, view):
        return True