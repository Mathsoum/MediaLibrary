from gallery.forms import ImageForm, AlbumForm
from gallery.utils import create_thumbnail  # , to_regular, to_hd, to_ImageField
from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Album, Image
from django.utils.text import slugify

# Create your views here.


def index(request):
    album_set = Album.objects.all()
    return render(request, 'gallery/index.html', locals())


def image_list(request):
    album_lst = Album.objects.all()
    image_lst = Image.objects.all()
    return render(request, 'gallery/image_list.html', locals())


def image_add(request):
    album_lst = Album.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, )
        if form.is_valid():
            image_instance = form.save()
            create_thumbnail(image_instance)
            image_instance.save()
            return redirect('gallery.views.album_detail', image_instance.album.slug)
    else:
        album_slug = request.GET.get('album_slug', '__')
        if album_slug == '__':
            print("Classic form")
            form = ImageForm()
        else:
            album = Album.objects.get(slug=album_slug)
            # print("album : %s // album slug : %s" % (album_slug, album_slug))
            form = ImageForm(initial={'album': album})

    return render(request, 'gallery/image_add.html', locals())


def image_del(request, album_slug, image_id):
    album = get_object_or_404(Album, slug=album_slug)
    album.image_set.filter(id=image_id).delete()
    return redirect('gallery.views.album_detail', slug=album_slug)


def album_list(request):
    album_lst = Album.objects.all()
    return render(request, 'gallery/album_list.html', locals())


def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)

        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.slug = slugify(new_album.title)
            new_album.save()
            return redirect('gallery.views.album_list')

    else:
        form = AlbumForm()

    return render(request, 'gallery/album_add.html', locals())


def album_detail(request, slug):
    album = get_object_or_404(Album, slug=slug)
    album_lst = Album.objects.all()
    return render(request, 'gallery/album_detail.html', locals())


def album_del(request, slug):
    album = get_object_or_404(Album, slug=slug)
    album.delete()
    return redirect('album_list', permanent=True)

