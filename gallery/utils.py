from PIL.Image import Image
from ZesteDeDjango_Advanced.settings import MEDIA_ROOT
from _io import StringIO
from django.core.files.base import ContentFile

thumbnail_size = (128,128)
hd_size = (1920, 1080)
regular_size = (1280, 720)

def to_thumbnail(image):
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "thumbnail/", image.name)
    return to_ImageField(image)
    
def to_regular(image):
    image.thumbnail(regular_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "regular/", image.name)
    
def to_hd(image):
    image.thumbnail(hd_size, Image.ANTIALIAS)
    image.save("%s%s%s" % MEDIA_ROOT, "1080p/", image.name)
     
def to_ImageField(pil_image, field_image):
    f = StringIO()
    try:
        pil_image.save(f, format='jpg')
        s = f.getvalue()
        field_image.save(field_image.name, ContentFile(s))
    finally:
        f.close()