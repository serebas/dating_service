from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from .serializers import LoverSerializer, ProfileSerializer
from .models import Lover
from .helpers import modified_photo

#http://127.0.0.1:8000/api/clients/create/
@api_view(['POST'])
def register_user(request):
    #сериализуем полученные данные
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
    
        #создаем пользователя
        user = User.objects.create_user(
            username=request.data['username'],
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            password=request.data['password'],
            email=request.data['email']
        )

        #создаем аккаунт этого пользователя c его фотографией
        lover = Lover.objects.create(
            user=user,
            gender=request.data['gender'],
            photo=request.data['photo']
        )

        #наносим на фото водяной знак, получаем новый путь к аватарке и сохраняем его в бд
        photo_path_with_watermark = modified_photo(lover.photo.url)
        lover.photo = photo_path_with_watermark
        lover.save()

        return Response({'message': 'account was created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientListAPIView(generics.ListAPIView):
    queryset = Lover.objects.all()
    serializer_class = LoverSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('gender', 'user__first_name', 'user__last_name')

