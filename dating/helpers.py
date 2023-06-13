from django.conf import settings
from PIL import Image

def modified_photo(photo_path):
    #получаем путь каталога приложения
    BASE_DIR = str(settings.BASE_DIR)

    #открываем фото и водяной знак
    photo = Image.open(BASE_DIR + photo_path)
    watermark = Image.open(BASE_DIR + '/watermark/watermark.png')

    #определяем положение водяного знака на аватарке (в центре)
    x = (photo.width - watermark.width) // 2
    y = (photo.height - watermark.height) // 2

    #создаем маску и делаем водяной знак прозрачным
    watermark_mask = watermark.convert('RGBA')
    watermark_mask = watermark_mask.point(lambda x: min(x, 85))

    #накладываем водяной знак на фото
    photo.paste(
        im=watermark,
        box=(x, y),
        mask=watermark_mask
    )

    #создаем путь к измененному фото и сохраняем его по этому пути
    changed_photo_path = photo_path.replace('.jpg', '_with_watermark.jpg')
    photo.save(BASE_DIR + changed_photo_path)

    photo.close()
    watermark.close()

    return changed_photo_path
