from PIL import Image
from MediaLibrary.settings import MEDIA_ROOT
from _io import BytesIO
from django.core.files.base import ContentFile

thumbnail_size = (128, 128)
hd_size = (1920, 1080)
regular_size = (1280, 720)


def open_image(path):
    return Image.open(path)


def create_thumbnail(image_model_instance):
    image_path = image_model_instance.original.name
    image_name = image_path.split('/').pop()
    pil_image = open_image(MEDIA_ROOT + image_path)
    pil_image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    f = BytesIO()
    try:
        pil_image.save(f, format=u'JPEG')
        s = f.getvalue()
        image_model_instance.thumbnail.save("thumb_%s" % image_name, ContentFile(s))
    finally:
        f.close()


def to_regular(image):
    image.thumbnail(regular_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "regular/", image.name)


def to_hd(image):
    image.thumbnail(hd_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "1080p/", image.name)
    
    