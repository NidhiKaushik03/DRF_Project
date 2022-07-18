from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Information, InformationSerializer
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet

class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

# class InformationListView(mixins.ListModelMixin, mixins.CreateModelMixin,  generics.GenericAPIView):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)



# class InformationDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)        

# class InformationListView(generics.ListAPIView,generics.ListCreateAPIView):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer



# class InformationDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer

# class InformationListView(generics.ListCreateAPIView):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer 

# class InformationDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Information.objects.all()
#     serializer_class = InformationSerializer

# class InformationViewSet(ViewSet):
#     def list(self, request):
#         courses = Information.objects.all()
#         serializer = InformationSerializer(courses, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = InformationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)    

#     def retrieve(self, request, pk):
#         try:
#             course = Information.objects.get(pk=pk)
#         except Information.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = InformationSerializer(course)
#         return Response(serializer.data)        