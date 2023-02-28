from django.shortcuts import render

# we need to set permissions for the endpoint we are set :
from rest_framework import permissions

# For Setting an endpoint based on a defined Model :
from rest_framework.viewsets import ModelViewSet

# importing the User and it's Serializer :
from Core.models import User
from Core.Serializers.serializers import UserSerializer

# Create your views here.

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated ]

    http_method_names = ['patch', 'get']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = User.objects.get(id=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
    

'''What to know to Understanding the code above:


    When using ModelViewSet class for defining an endpoint:
        * The get_queryset() method is used to get a list of all the objects of the requested Model.
            in our case, the Api will look like : /api/user

        * The get_object() method is used to get a specific object from a Model:
            In this case, the Api url will look like this : /api/user/<id>
            where <id> will identify the specific object 

'''
