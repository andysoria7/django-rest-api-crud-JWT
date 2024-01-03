from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import TaskSerializer
from .models import Task
from django.utils import timezone

# Create your views here.

@extend_schema_view(
    list = extend_schema(description='Permite obtener una lista de tareas.'),
    retrieve = extend_schema(description='Permite obtener una tarea.'),
    create = extend_schema(description='Permite crear una tarea.'),
    update = extend_schema(description='Permite actualizar una tarea.'),
    destroy = extend_schema(description='Permite eliminar una tarea.'),
    
)
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    @extend_schema(
        parameters=[{
            'name': 'created_at',
            'in': 'query',
            'description': 'Fecha de creación en formato YYYY-MM-DD',
            'required': False,
            'type': 'string',
            'format': 'date',
        }],
        responses={200: TaskSerializer(many=True)}
    )
    @action(detail=False, methods=['post'])
    def filter_by_creation_date_with_body(self, request):
        print(request.data)  # Agrego este print para ver el contenido del cuerpo de la solicitud en la consola
        created_at = request.data.get('created_at')
        print(f'created_at: {created_at}')  # Agrego este print para ver el valor de created_at
    
        if created_at:
            tasks = Task.objects.filter(created_at__date=created_at)
            serializer = self.get_serializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Debes proporcionar la fecha de creación en el cuerpo de la solicitud.'}, status=400)