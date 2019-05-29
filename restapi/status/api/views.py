#from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StatusSerializer
from status.models import Status

from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404
import json

#for authentication and permissions import below two
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions

#for IsOwnerOrReadOnly permission
from accounts.api.permissions import IsOwnerOrReadOnly

def is_json(json_data):
    try:
        real_json=json.loads(json_data)
        is_valid=True
    except ValueError:
        is_valid=False
    return is_valid


#for image updating and deleting
class StatusAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    # we can comment out both of these if we implement the it globally in main.py file reconf folder
    permission_classes=[permissions.IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes=[]

    #queryset=Status.object.all()
    serializer_class=StatusSerializer
    queryset=Status.object.all()
    lookup_field='id'


    #to update data
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #to do the partial changes to the existing object
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #to delete data
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    # we can comment out both of these if we implement the it globally in main.py file reconf folder
    permission_classes=[permissions.IsAuthenticated]
    # authentication_classes=[SessionAuthentication]

    #for search and ordering
    search_fields=('user__username', 'content')
    ordering_fields=('user__username', 'timestamp')
    queryset=Status.object.all()
    #queryset=Status.object.all()
    serializer_class=StatusSerializer
    passed_id = None
    #This is all about get the list of objects and get object by its id
    #comment this out because we implement search & ordering by in built methods
    # def get_queryset(self):
    #     request=self.request
    #     #print(request.user)
    #     qs=Status.object.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(content__icontains=query)
    #     return qs

    #to create data
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





#view for only one endpoint........this one is old & above is new
# class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     permission_classes=[]
#     authentication_classes=[]
#     #queryset=Status.object.all()
#     serializer_class=StatusSerializer
#     passed_id = None
#     #This is all about get the list of objects and get object by its id
#     def get_queryset(self):
#         request=self.request
#         qs=Status.object.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     def get_object(self):
#         request=self.request
#         passed_id=request.GET.get('id', None) or self.passed_id
#         queryset=self.get_queryset()
#         obj=None
#         if passed_id is not None:
#             obj=get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj
#
#     def get(self, request, *args, **kwargs):
#         url_passed_id=request.GET.get('id', None)
#         json_data={}
#         body_=request.body
#         if is_json(body_):
#             json_data=json.loads(request.body)
#         new_passed_id=json_data.get('id', None)
#         #print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         if passed_id is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)
#     ###########################################################################
#
#
#     #to create data
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     #to update data
#     def put(self, request, *args, **kwargs):
#         #after creating the python script to call our api
#         url_passed_id=request.GET.get('id', None)
#         json_data={}
#         body_=request.body
#         if is_json(body_):
#             json_data=json.loads(request.body)
#         new_passed_id=json_data.get('id', None)
#         #print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         ##################################################
#         return self.update(request, *args, **kwargs)
#
#     #to do the partial changes to the existing object
#     def patch(self, request, *args, **kwargs):
#         #after creating the python script to call our api
#         url_passed_id=request.GET.get('id', None)
#         json_data={}
#         body_=request.body
#         if is_json(body_):
#             json_data=json.loads(request.body)
#         new_passed_id=json_data.get('id', None)
#         #print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         ###################################################
#         return self.update(request, *args, **kwargs)
#
#     #to delete data
#     def delete(self, request, *args, **kwargs):
#         #after creating the python script to call our api
#         url_passed_id=request.GET.get('id', None)
#         json_data={}
#         body_=request.body
#         if is_json(body_):
#             json_data=json.loads(request.body)
#         new_passed_id=json_data.get('id', None)
#         #print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         ###################################################
#         return self.destroy(request, *args, **kwargs)













# class StatusListAPIView(APIView):
#     permission_classes=[]
#     authentication_classes=[]
#
#     def get(self, request, format=None):
#         qs=Status.object.all()
#         serializer=StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         qs=Status.object.all()
#         serializer=StatusSerializer(qs, many=True)
#         return Response(serializer.data)
#
# #CreateModelMixin is for post data
# class StatusAPIView(generics.ListAPIView, mixins.CreateModelMixin):
#     permission_classes=[]
#     authentication_classes=[]
#     #queryset=Status.object.all()
#     serializer_class=StatusSerializer
#
#     def get_queryset(self):
#         qs=Status.object.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs
#
#     #to create data
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# # class StatusCreateAPIView(generics.CreateAPIView):
# #     permission_classes=[]
# #     authentication_classes=[]
# #
# #     queryset=Status.object.all()
# #     serializer_class=StatusSerializer
#
# class StatusDetailAPIView(generics.RetrieveAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     permission_classes=[]
#     authentication_classes=[]
#
#     queryset=Status.object.all()
#     serializer_class=StatusSerializer
#     #lookup_field='id'
#
#     #to update data
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     #to delete data
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# #functionality is same as above class with the use of RetrieveUpdateDestroyAPIView
# # class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
# #     permission_classes=[]
# #     authentication_classes=[]
# #
# #     queryset=Status.object.all()
# #     serializer_class=StatusSerializer
#
#
# # class StatusUpdateAPIView(generics.UpdateAPIView):
# #     permission_classes=[]
# #     authentication_classes=[]
# #
# #     queryset=Status.object.all()
# #     serializer_class=StatusSerializer
#
#
# # class StatusDeleteAPIView(generics.DestroyAPIView):
# #     permission_classes=[]
# #     authentication_classes=[]
# #
# #     queryset=Status.object.all()
# #     serializer_class=StatusSerializer
