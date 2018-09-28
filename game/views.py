from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from serializers import ProcessSerializer
from models import *
from random import randint
import time, json, datetime
import copy
import utils

class ProcessView(generics.ListCreateAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def get(self, request, *args, **kwargs):
        process = Process.objects.all()
        serializer = ProcessSerializer(process, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProcessSerializer(data=request.data, partial=True)
        duration = randint(15, 31)
        header = request.META
        path = request.META.get("PATH_INFO")
        method_type = request.META.get("REQUEST_METHOD")
        query = request.META.get("QUERY_STRING")
        current_time = datetime.datetime.now()
        if serializer.is_valid():
            serializer.save(duration=duration, header=str(header), body=request.data.get("body"),
                            method_type=method_type, query=query,
                            time=current_time, path=path)
            time.sleep(duration)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProcessDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    """Retrieve, update or delete a process instance."""

    def get_object(self, pk):
        try:
            return Process.objects.get(pk=pk)
        except Process.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        process = self.get_object(pk)
        serializer = ProcessSerializer(process)
        data = serializer.data
        data["method_type"] = request.META["REQUEST_METHOD"]
        update_data = copy.deepcopy(data)
        update_data.pop("id")
        duration = randint(15, 31)
        update_data["duration"] = duration
        current_time = datetime.datetime.now()
        update_data["time"] = current_time
        serializer = ProcessSerializer(data=update_data)
        if serializer.is_valid():
            serializer.save()
            time.sleep(duration)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        process = self.get_object(pk)
        request.data['id'] = process.id
        serializer = ProcessSerializer(process, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        data = serializer.data
        data["method_type"] = request.META["REQUEST_METHOD"]
        update_data = copy.deepcopy(data)
        update_data.pop("id")
        duration = randint(15, 31)
        update_data["duration"] = duration
        current_time = datetime.datetime.now()
        update_data["time"] = current_time
        serializer = ProcessSerializer(data=update_data)
        if serializer.is_valid():
            serializer.save()
            time.sleep(duration)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        process = self.get_object(pk)
        serializer = ProcessSerializer(process)
        data = serializer.data
        data["method_type"] = request.META["REQUEST_METHOD"]
        update_data = copy.deepcopy(data)
        update_data.pop("id")
        current_time = datetime.datetime.now()
        update_data["time"] = current_time
        serializer = ProcessSerializer(data=update_data)
        if serializer.is_valid():
            serializer.save()
        process.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        process = Process.objects.all()
        serializer = ProcessSerializer(process, many=True)
        data =  serializer.data
        response = utils.get_stat_response(data)

        return Response(response)


