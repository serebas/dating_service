from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import LoverSerializer
from .models import Lover
from .helpers import modified_photo

#http://127.0.0.1:8000/api/clients/create/
@api_view(['POST'])
def register_user(request):
    #сериализуем полученные данные
    serializer = LoverSerializer(data=request.data)
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