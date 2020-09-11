from rest_framework import viewsets
from .models import Movies , Genre
from .serializers import MoviesSerializer , GenreSerializer
from rest_framework.response import Response
from rest_framework import status


class MoviesViewset(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    # to list all movies or filter
    def list(self, request):
        search = str(self.request.query_params.get('search', None))
        if 'search' in self.request.query_params:
            queryset = Movies.objects.filter(name__startswith=search)
            serializer = MoviesSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Movies.objects.all()
            serializer = MoviesSerializer(queryset, many=True)
            return Response(serializer.data)

    # to create movie
    def create(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"status":401,"message":"Unauthorized Access Only Admin has access of Create"})

    # to update movie
    def update(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({"status": 401, "message": "Unauthorized Access Only Admin has access of Update"})

    # to delete movie
    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"status": 401, "message": "Unauthorized Access Only Admin has access of Delete"})


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # to list all genre
    def list(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)

    # to create genre
    def create(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"status":401,"message":"Unauthorized Access Only Admin has access of Create"})

    # to update genre
    def update(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response({"status": 401, "message": "Unauthorized Access Only Admin has access of Update"})

    # to delete genre
    def destroy(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"status": 401, "message": "Unauthorized Access Only Admin has access of Delete"})


