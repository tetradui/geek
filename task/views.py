from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer




@api_view(['GET'])
def get_tasks(request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['GET', 'DELETE'])
def get_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'GET':
        serializer = TaskSerializer(instance=task)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        title_product = task.title
        task.delete()
        return Response('deleted', status=204)


@api_view(['PATCH', 'PUT'])
def update_task(request, id):
    product = get_object_or_404(Task, id=id)
    if request.method == 'PATCH':
        serializer = TaskSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('edited little', status=200)

    elif request.method == 'PUT':
        serializer = TaskSerializer(instance=product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('edited', status=200)
