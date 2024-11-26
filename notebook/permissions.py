from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Sadece nesnenin sahibi olan kullanicinin ulaşmasi için izin verilir.
    """

    def has_permission(self, request, view):
        # Check that the user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Verify that the object contains the "user" field and that the user is the owner
        if not hasattr(obj, 'user'):
            return False
        return obj.user == request.user

