from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from .models import Teachers, Students
from rest_framework.response import Response
from .serializers import TeacherSerializers, StudentSerializers
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins, permissions


class TeacheraAPIVIEW(APIView):
    def get(self, request, format=None):
        teacher_objs = Teachers.teacher_manager.all()
        serializer = TeacherSerializers(teacher_objs, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializers = TeacherSerializers(data=request_data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        print(request_data)
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class TeacherDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            teacher_obj = Teachers.teacher_manager.get(pk=pk)
        except Teachers.DoesNotExist as ex:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializers = TeacherSerializers(obj)
        return Response(serializers.data)

    def delete(self, request, pk, format=None):
        teacher_obj = self.get_object(pk)
        teacher_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        request_data = request.data
        serializer = TeacherSerializers(obj, request_data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            eror = serializer.errors
            return Response(f"Xato malumotlar kiritilgan {list(eror.keys()[0])} {list(eror.values())[0]}",
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        obj = self.get_object(pk)
        request_data = request.data
        serializer = TeacherSerializers(obj, request_data, partial=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            eror = serializer.errors
            return Response(f"Xato malumotlar kiritilgan {list(eror.keys()[0])} {list(eror.values())[0]}",
                            status=status.HTTP_400_BAD_REQUEST)


class StudentLisCReteAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             generics.GenericAPIView,
                             ):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields =['id']
    # pagination_class = [StandardResultsSetPagination]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StudentRetrieveAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
