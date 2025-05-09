from rest_framework.permissions import BasePermission

class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.sistema == 'P'
    
class IsDisciplina(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.sistema == 'D'

class IsAmbiente(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.sistema == 'A'
