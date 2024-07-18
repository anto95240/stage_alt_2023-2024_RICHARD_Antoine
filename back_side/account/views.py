from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer

# Vue pour l'inscription
@api_view(['POST'])
@permission_classes([AllowAny])  # Autoriser l'inscription sans authentification
def role_register(request, role):
    data = request.data
    email = data.get('Email')
    password1 = data.get('password1')
    password2 = data.get('password2')
    address = data.get('Address')
    first_name = data.get('FirstName')
    last_name = data.get('LastName')

    if password1 != password2:
        return Response({'success': False, 'message': 'Les mots de passe ne correspondent pas'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(Email=email).exists():
        return Response({'success': False, 'message': 'Un utilisateur avec cet email existe déjà'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        hashed_password = make_password(password1)
        user = User.objects.create(
            Email=email,
            Password=hashed_password,
            Role=role,
            Address=address,
            FirstName=first_name,  # Ajoutez ces lignes pour enregistrer le prénom et le nom
            LastName=last_name
        )
        serializer = UserSerializer(user)

        # Création de JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            'success': True,
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Vue pour la connexion
@api_view(['POST'])
@permission_classes([AllowAny])  # Autoriser la connexion sans authentification
def role_login(request, role):
    email = request.data.get('Email')
    password = request.data.get('password')

    try:
        user = User.objects.get(Email=email, Role=role)
        if check_password(password, user.Password):
            serializer = UserSerializer(user)

            # Création de JWT
            refresh = RefreshToken.for_user(user)
            response = Response({
                'success': True,
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)

            # Définir les cookies
            response.set_cookie('FirstName', user.FirstName)
            response.set_cookie('LastName', user.LastName)

            return response
        else:
            return Response({'success': False, 'message': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'success': False, 'message': 'L\'utilisateur n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Autoriser seulement les utilisateurs authentifiés
def get_user_details(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)