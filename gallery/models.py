from django.db import models
from MediaLibrary.settings import MEDIA_URL
import json

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    def get_images_as_json(self):
        raw_data = []
        for image in self.image_set.all():
            raw_data.append(
                {
                    "image": MEDIA_URL + image.original.name,
                    "title": image.title,
                    "description": image.description,
                    "thumbnail": MEDIA_URL + image.thumbnail.name,
                }
            )

        print("Raw data : %s" % json.dumps(raw_data, indent=4, sort_keys=True))

        return json.dumps(raw_data)


class Image(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)

    original = models.ImageField(upload_to="original/")
    # image = models.ImageField(upload_to="regular/", editable=False)
    thumbnail = models.ImageField(upload_to="thumbnail/", editable=False)
    # big = models.ImageField(upload_to="1080p/", editable=False)
    #     layer = models.CharField(max_length=256, default="")

    album = models.ForeignKey(Album)

    def __str__(self):
        return self.title

    def get_json_data(self):
        data = {
            'description': ("%s" % self.description),

            #             'layer': ("%s" % self.layer.name),
        }
        return json.loads(data)


