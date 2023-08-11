from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

from users.models import ConfirmationCode, generate_confirmation_code
from .serializers import AuthorizationValidateSerializer, RegistrationValidateSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def registration_api_view(request):
    serializer = RegistrationValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')
    user = User.objects.create_user(username=username, password=password, is_active=False)

    code = generate_confirmation_code()
    confirmation_code = ConfirmationCode.objects.create(user=user, code=code)

    return Response(status=201, data={'user_id': user.id})


@api_view(['POST'])
def user_confirmation_api_view(request):
    code = request.data.get('code')
    try:
        confirmation_code = ConfirmationCode.objects.get(code=code)
        user = confirmation_code.user
        user.is_active = True
        user.save()
        confirmation_code.delete()
        return Response(status=200, data={'message': 'User confirmed successfully.'})
    except ConfirmationCode.DoesNotExist:
        return Response(status=400, data={'message': 'Invalid confirmation code.'})


# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = RegistrationValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#     user = User.objects.create_user(username=username, password=password, is_active=False)
#     return Response(status=201, data={'user_id':user.id})


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