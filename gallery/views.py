from gallery.forms import ImageForm, AlbumForm
# from gallery.utils import to_thumbnail, to_regular, to_hd, to_ImageField
from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Album, Image
from django.utils.text import slugify

# Create your views here.

def image_list(request):
    album_list = Album.objects.all()
    image_list = Image.objects.all()
    return render(request, 'gallery/image_list.html', locals())
    
def image_add(request):
    album_list = Album.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('gallery.views.image_list', permanent=True)
    else:
        album_slug = request.GET.get('album_slug', '__')
        if album_slug == '__':
            print("Classic form")
            form = ImageForm()
        else:
            album = Album.objects.get(slug=album_slug)
            print("album : %s // album slug : %s" % (album_slug, album_slug))
            form = ImageForm(initial={'album': album}) # Album.objects.get(slug=album_slug).title
        
    return render(request, 'gallery/image_add.html', locals())

def album_list(request):
    album_list = Album.objects.all()
    return render(request, 'gallery/album_list.html', locals())
    
def album_add(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        
        if form.is_valid():
            new_album = form.save(commit=False)
            new_album.slug = slugify(new_album.title)
            new_album.save()
            return redirect('gallery.views.album_list', permanent=True)
            
    else:
        form = AlbumForm()
        
    return render(request, 'gallery/album_add.html', locals())
        
def album_detail(request, slug):
    album = get_object_or_404(Album, slug=slug)
    return render(request, 'gallery/album_detail.html', locals())

