from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from gallery.forms import ImageForm, AlbumForm, ConnexionForm, UserCreationForm
from gallery.utils import create_thumbnail  # , to_regular, to_hd, to_ImageField
from django.shortcuts import render, redirect, get_object_or_404
from gallery.models import Album, Image
from django.utils.text import slugify
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'gallery/index.html')


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)
        messages.success(request, 'You have been logged out successfully !')

    return redirect('index', permanent=True)


def user_add(request):
    error = False

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['firstName']
            last_name = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            messages.success(request, 'Account created. You can now log in.')
            return render(request, 'gallery/index.html', locals())
    else:
        form = UserCreationForm()

    return render(request, 'gallery/user_add.html', locals())


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Welcome %s. You are now logged in =)' % user.username)
        else:
            messages.error(request, 'Authentication failed with this username and password.')
            return redirect('Connexion view')

    return redirect('index')


def connexion_view(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            connexion(request)
    else:
        form = ConnexionForm()

    return render(request, 'gallery/connexion.html', locals())


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
    return render(request, 'gallery/album_detail.html', locals())

