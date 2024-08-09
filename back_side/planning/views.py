from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer
from user.models import *
from user.serializers import *

# vue pour récupérer les cours en fonction du rôle et de l'utilisateur
@api_view(['GET'])
def get_courses(request):
    user_id = request.query_params.get('user_id')
    role = request.query_params.get('role')
    
    if not user_id or not role:
        return Response({'error': 'user_id et role sont requis'}, status=400)
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=404)
    
    if role == 'student':
        courses = Course.objects.filter(
            class_level=user.classe,
            specialization=user.specialization
        )
    elif role == 'teacher':
        courses = Course.objects.filter(
            teacher=user
        )
    else:
        return Response({'error': 'Rôle non valide'}, status=400)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# vue pour rechercher des étudiants en fonction de différents critères
@api_view(['GET'])
def search_students(request):
    role = request.GET.get('role', None)
    class_level = request.GET.get('class_level', None)
    specialization = request.GET.get('specialization', None)
    intervenant = request.GET.get('intervenant', None)
    start_time = request.GET.get('start_time', None)
    end_time = request.GET.get('end_time', None)

    if class_level and not class_level.isdigit():
        return JsonResponse({'error': 'Invalid class level'}, status=400)
    if specialization and not specialization.isdigit():
        return JsonResponse({'error': 'Invalid specialization'}, status=400)
    if intervenant and not intervenant.isdigit():
        return JsonResponse({'error': 'Invalid intervenant'}, status=400)

    class_level = int(class_level) if class_level else None
    specialization = int(specialization) if specialization else None
    intervenant = int(intervenant) if intervenant else None

    filters = {}
    if role:
        filters['role'] = role
    if class_level is not None:
        filters['class_level'] = class_level
    if specialization is not None:
        filters['specialization'] = specialization
    if intervenant is not None:
        filters['intervenant'] = intervenant
    if start_time:
        filters['start_time__gte'] = start_time
    if end_time:
        filters['end_time__lte'] = end_time

    try:
        plannings = Course.objects.filter(**filters)
        data = list(plannings.values())
        return JsonResponse({'plannings': data})
    except Exception as e:
        return JsonResponse({'error': 'Erreur lors de la recherche'}, status=500)

