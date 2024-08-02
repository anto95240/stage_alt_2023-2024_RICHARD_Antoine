from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from user.models import User
from .serializers import CourseSerializer

@api_view(['GET'])
def get_courses(request):
    # Obtenir les paramètres de la requête
    user_id = request.query_params.get('user_id')
    role = request.query_params.get('role')
    
    if not user_id or not role:
        return Response({'error': 'user_id et role sont requis'}, status=400)
    
    # Récupérer l'utilisateur en fonction de l'id
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé'}, status=404)
    
    # Filtrer les cours en fonction du rôle
    if role == 'student':
        # Filtrer les cours en fonction de la classe et spécialité de l'utilisateur
        courses = Course.objects.filter(
            ClassLevel=user.Class,
            Specialization=user.Specialization
        )
    elif role == 'teacher':
        # Filtrer les cours enseignés par l'utilisateur
        courses = Course.objects.filter(
            Teacher=user
        )
    else:
        return Response({'error': 'Rôle non valide'}, status=400)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
