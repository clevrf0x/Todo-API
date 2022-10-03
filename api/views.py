from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Task
from api.serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'All Task List': '/task-list/ (GET)',
    'Task Detail View': '/task-view/<str:pk>/ (GET)',
    'Task Create': '/task-create/ (POST)',
    'Task Update': '/task-update/<str:pk>/ (POST)',
    'Task Delete': '/task-delete/<str:pk>/ (DELETE)',
    'Task Progress': '/task-progress/ (GET)',
    'Task Completed': '/task-completed/ (GET)'
  }
  return Response(api_urls)

@api_view(['GET'])
def taskList(request):
  tasks = Task.objects.all()
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def taskView(request, id):
  task = Task.objects.get(id=id)
  serializer = TaskSerializer(task, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
  serializer = TaskSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, id):
  task = Task.objects.get(id=id)
  serializer = TaskSerializer(instance=task, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return Response('Item deleted successfully')

@api_view(['GET'])
def taskProgress(request):
  tasks = Task.objects.filter(completed=False)
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def taskCompleted(request):
  tasks = Task.objects.filter(completed=True)
  serializer = TaskSerializer(tasks, many=True)
  return Response(serializer.data)