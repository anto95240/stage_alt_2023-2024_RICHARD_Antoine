import base64
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer
from planning.models import *
from planning.serializers import *
from django.http import JsonResponse

# Vue pour l'inscription
@api_view(['POST'])
@permission_classes([AllowAny])
def role_register(request, role):
    data = request.data
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    address = data.get('address')
    email = data.get('email')
    password1 = data.get('password1')
    password2 = data.get('password2')

    # Vérifier si tous les champs sont présents
    if not all([first_name, last_name, address, email, password1, password2]):
        return Response({"success": False, "message": "Tous les champs sont requis"}, status=status.HTTP_400_BAD_REQUEST)

    if password1 != password2:
        return Response({'success': False, 'message': 'Les mots de passe ne correspondent pas'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'success': False, 'message': 'Un utilisateur avec cet email existe déjà'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(
            email=email,
            password=password1,
            role=role,
            address=address,
            first_name=first_name,
            last_name=last_name
        )
        
        response = Response({
            'success': True,
            'user': UserSerializer(user).data,
        }, status=status.HTTP_200_OK)

        response.set_cookie('FirstName', user.first_name, secure=True, samesite='Strict')
        response.set_cookie('LastName', user.last_name, secure=True, samesite='Strict')
        response.set_cookie('UserId', user.id, secure=True, samesite='Strict')
        
        return response
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Vue pour la connexion
@api_view(['POST'])
@permission_classes([AllowAny])
def role_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not all([email, password]):
        return Response({'success': False, 'message': 'L\'email et le mot de passe sont requis'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            response = Response({
                'success': True,
                'user': UserSerializer(user).data,
            }, status=status.HTTP_200_OK)

            response.set_cookie('FirstName', user.first_name, secure=True, samesite='Strict')
            response.set_cookie('LastName', user.last_name, secure=True, samesite='Strict')
            response.set_cookie('UserId', user.id, secure=True, samesite='Strict')
            
            return response
        else:
            return Response({'success': False, 'message': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'success': False, 'message': 'L\'utilisateur n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

# Vue pour la déconnexion
@api_view(['POST'])
def logout_view(request):
    response = Response({"success": True, "message": "Déconnexion réussie"}, status=status.HTTP_200_OK)
    response.delete_cookie('csrftoken')
    response.delete_cookie('sessionid')
    response.delete_cookie('FirstName')
    response.delete_cookie('LastName')
    response.delete_cookie('UserId')
    return response

# Vue pour obtenir les détails utilisateur
@api_view(['GET'])
def user_info(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user_info = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "address": user.address,
            "email": user.email,
            "age": user.age,
            "photo": None,
            "specialization": user.specialization.specialization if user.specialization else None,
            "classe": user.classe.classe if user.classe else None,
        }
        if user.photo:
            with open(user.photo.path, "rb") as image_file:
                photo_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                user_info['Photo'] = photo_base64
        else:
            user_info['Photo'] = None
            
        return JsonResponse(user_info)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Utilisateur non trouvé'}, status=404)

# Vue pour la mise à jour de l'utilisateur
@api_view(['PUT'])
def user_update(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = request.data
        
        if 'password' in data and data['password']:
            user.password = make_password(data['password'])
        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        if 'address' in data:
            user.address = data['address']
        if 'email' in data:
            user.email = data['email']
        if 'age' in data:
            user.age = data['age']
        if 'photo' in request.FILES:
            user.photo = request.FILES['photo']
        
        user.save()
        return Response({'message': 'Informations mises à jour avec succès'}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Une erreur est survenue lors de la mise à jour.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)