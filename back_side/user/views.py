import base64
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.http import JsonResponse


# Vue pour l'inscription
@api_view(['POST'])
@permission_classes([AllowAny])
def role_register(request, role):
    data = request.data
    first_name = data.get('FirstName')
    last_name = data.get('LastName')
    address = data.get('Address')
    email = data.get('Email')
    password1 = data.get('Password1')
    password2 = data.get('Password2')

    # Vérifier si tous les champs sont présents
    if not all([first_name, last_name, address, email, password1, password2]):
        return Response({"success": False, "message": "Tous les champs sont requis"}, status=status.HTTP_400_BAD_REQUEST)

    if password1 != password2:
        return Response({'success': False, 'message': 'Les mots de passe ne correspondent pas'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(Email=email).exists():
        return Response({'success': False, 'message': 'Un utilisateur avec cet email existe déjà'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(
            Email=email,
            Password=password1,
            Role=role,
            Address=address,
            FirstName=first_name,
            LastName=last_name
        )
        
        response = Response({
            'success': True,
            'user': UserSerializer(user).data,
        }, status=status.HTTP_200_OK)

        response.set_cookie('FirstName', user.FirstName, secure=True, samesite='Strict')
        response.set_cookie('LastName', user.LastName, secure=True, samesite='Strict')
        response.set_cookie('UserId', user.id, secure=True, samesite='Strict')        
        
        return response
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Vue pour la connexion
@api_view(['POST'])
@permission_classes([AllowAny])
def role_login(request):
    email = request.data.get('Email')
    password = request.data.get('Password')

    if not all([email, password]):
        return Response({'success': False, 'message': 'L\'email et le mot de passe sont requis'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(Email=email)
        if check_password(password, user.Password):
            response = Response({
                'success': True,
                'user': UserSerializer(user).data,
            }, status=status.HTTP_200_OK)

            response.set_cookie('FirstName', user.FirstName, secure=True, samesite='Strict')
            response.set_cookie('LastName', user.LastName, secure=True, samesite='Strict')
            response.set_cookie('UserId', user.id, secure=True, samesite='Strict')
            
            return response
        else:
            return Response({'success': False, 'message': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'success': False, 'message': 'L\'utilisateur n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

# Vue pour obtenir les détails utilisateur
@api_view(['GET'])
def user_info(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        user_info = {
            "FirstName": user.FirstName,
            "LastName": user.LastName,
            "Address": user.Address,
            "Email": user.Email,
            "Age": user.Age,
            "Photo": None,
            "Specialization": user.Specialization,
        }
        if user.Photo:
            with open(user.Photo.path, "rb") as image_file:
                photo_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                user_info['Photo'] = photo_base64
        else:
            user_info['Photo'] = None
            
        return JsonResponse(user_info)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Utilisateur non trouvé'}, status=404)

# Vue pour mettre à jour les détails utilisateur
# @api_view(['PUT'])
# def user_update(request):
#     user = request.user
    
#     data = request.data
#     serializer = UserSerializer(user, data=data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'success': True, 'user': serializer.data}, status=status.HTTP_200_OK)
#     return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# views.py
@api_view(['PUT'])
def user_update(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        data = request.data
        
        if 'Password' in data and data['Password']:
            user.Password = make_password(data['Password'])
        if 'FirstName' in data:
            user.FirstName = data['FirstName']
        if 'LastName' in data:
            user.LastName = data['LastName']
        if 'Address' in data:
            user.Address = data['Address']
        if 'Email' in data:
            user.Email = data['Email']
        if 'Age' in data:
            user.Age = data['Age']
        if 'Specialization' in data:
            user.Specialization = data['Specialization']
        
        # Handle photo file upload
        if 'Photo' in request.FILES:
            user.Photo = request.FILES['Photo']
        
        user.save()
        return Response({'message': 'Informations mises à jour avec succès'}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'error': 'Utilisateur non trouvé.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Une erreur est survenue lors de la mise à jour.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)