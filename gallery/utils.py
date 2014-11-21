from PIL import Image
from MediaLibrary.settings import MEDIA_ROOT
from _io import StringIO
from django.core.files.base import ContentFile
import os

thumbnail_size = (128,128)
hd_size = (1920, 1080)
regular_size = (1280, 720)

def open_image(path):
    return Image.open(path)

def to_ImageField(pil_image, field_image):
    f = StringIO()
    try:
        pil_image.save(f, format='JPEG')
        s = f.getvalue()
        field_image.save(field_image.name, ContentFile(s))
    finally:
        f.close()

def to_thumbnail(field_image):
    image_path = field_image.name
    image_name = image_path.split('/').pop()
    image_filename, image_ext = os.path.splitext(image_name)
    pil_image = open_image(MEDIA_ROOT + image_path)
    pil_image.thumbnail(thumbnail_size, Image.ANTIALIAS)
    pil_image.save("%s%sthumb_%s" % (MEDIA_ROOT, "thumbnail/", image_filename), u'JPEG')
    return to_ImageField(pil_image, field_image)
    
def to_regular(image):
    image.thumbnail(regular_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "regular/", image.name)
    
def to_hd(image):
    image.thumbnail(hd_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "1080p/", image.name)
    
    