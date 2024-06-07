from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *

class CarsListViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers

    # def get(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True, context={'request': request})
    #     return Response(serializer.data, status=status.'HTTS_200_OK)


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers
    lookup_field = 'id'



class MovieCreateView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializers

















