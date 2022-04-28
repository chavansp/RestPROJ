from django.shortcuts import render
# from rest_framework import viewsets
#from django.contrib.auth.models import User
from .serializer import UserLoginSerializer
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .renderers import UserRenderer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
# class Userview(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [IsAuthenticated]
#

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class UserLoginView(TokenObtainPairView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    print(request.data)
    serializer = UserLoginSerializer(data=request.data)
    print(serializer)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    password = serializer.data.get('password')
    print(username)
    user = authenticate(username=username, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['username or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class logoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)