from rest_framework.permissions import BasePermission
class IsAdmin(BasePermission):
    def has_permission(self,req,view):
        if req.method in ['GET','HEAD','OPTIONS']:
            return True
        return req.user.is_staff