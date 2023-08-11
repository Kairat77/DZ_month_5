from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import AuthorizationValidateSerializer, RegistrationValidateSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegistrationValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    user = User.objects.create_user(username=username, password=password, is_active=False)
    return Response(status=201, data={'user_id':user.id})


@api_view(['POST'])
def authorization_api_view(request):
    # 0. Step: Validation
    serializer = AuthorizationValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # 2. Step: Search user by credentials
    user = authenticate(**serializer.validated_data)
    # 3. Return Key
    if user is not None:
         token_, created = Token.objects.get_or_create(user=user)
         return Response(data={'key': token_.key})
    # 4. Return Error
    else:
      return Response(status=401, data={'message':'User not found'})