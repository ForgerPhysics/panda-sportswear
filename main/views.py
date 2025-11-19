from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime
from django.utils.html import strip_tags
from django.contrib.auth.models import User
import requests
# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    # product_list= Product.objects.all()

    context = {
        'namaaplikasi' : 'Panda Sportswear',
        'nama': 'Ryan Gibran Purwacakra Sihaloho',
        'kelas': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def show_xml(request):
    product_list=Product.objects.all()
    xml_data=serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    # product_list= Product.objects.all()
    # json_Data=serializers.serialize("json", product_list)
    # return HttpResponse(json_Data, content_type="application/json")
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'product_views' : product.product_views,
            'stock': product.stock,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user': product.user.username if product.user else None,
            # berdasarkan field pada models.py
            # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            # name = models.CharField(max_length=60)
            # price = models.IntegerField()
            # description = models.TextField()
            # thumbnail = models.URLField(blank=True, null=True)
            # category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='update')
            # is_featured = models.BooleanField(default=False)
            # product_views = models.PositiveIntegerField(default=0)
            # stock = models.IntegerField()
            # created_at = models.DateTimeField(auto_now_add=True)
            # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, news_id):
    try:
        product_item=Product.objects.filter(pk=news_id)
        xml_data=serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, news_id):
    # try: 
    #     product_item = Product.objects.get(pk=news_id)
    #     json_data = serializers.serialize("json", [product_item])
    #     return HttpResponse(json_data, content_type="application/json")
    # except Product.DoesNotExist:
    #     return HttpResponse(status=404)
    try:
        product = Product.objects.select_related('user').get(pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def create_product(request):
    # form = ProductForm(request.POST or None)

    # if form.is_valid() and request.method == "POST":
    #     form.save()
    #     return redirect('main:show_main')

    # context = {'form': form}
    # return render(request, "create_product.html", context)
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        # if form.is_valid():
        #     user = form.get_user()
        #     login(request, user)
        #     return redirect('main:show_main')
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
@login_required
def add_product_ajax(request):
    try:
        name = strip_tags(request.POST.get("name"))
        price = int(request.POST.get("price"))
        description = strip_tags(request.POST.get("description"))
        category = request.POST.get("category")
        thumbnail = request.POST.get("thumbnail", "")
        is_featured = request.POST.get("is_featured") == 'on'
        stock = int(request.POST.get("stock", 0))

        # Validasi kategori
        valid_categories = [c[0] for c in Product.CATEGORY_CHOICES]
        if category not in valid_categories:
            return JsonResponse({"error": "Kategori tidak valid."}, status=400)

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            stock=stock,
            user=request.user,
        )

        return JsonResponse({"message": "Produk berhasil disimpan!"}, status=201)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({"error": "Terjadi kesalahan saat menyimpan produk."}, status=400)


@csrf_exempt
@require_POST
@login_required
def edit_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id, user=request.user)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)
        
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Produk berhasil diperbarui!'})
        else:
            print("🧩 FORM ERRORS:", form.errors.as_json()) 
            return JsonResponse({'error': 'Form tidak valid'}, status=400)
    
    return JsonResponse({'error': 'Metode tidak diizinkan'}, status=405)


@csrf_exempt
@require_POST
@login_required
def delete_product_ajax(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
        product.delete()
        return JsonResponse({'message': 'Produk berhasil dihapus!'})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Produk tidak ditemukan.'}, status=404)
    
def ajax_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login berhasil!'})
        else:
            return JsonResponse({'success': False, 'message': 'Username atau password salah.'})
    return JsonResponse({'success': False, 'message': 'Metode tidak valid.'}, status=400)


def ajax_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return JsonResponse({'success': False, 'message': 'Password tidak cocok.'})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username sudah digunakan.'})

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({'success': True, 'message': 'Registrasi berhasil! Silakan login.'})

    return JsonResponse({'success': False, 'message': 'Metode tidak valid.'}, status=400)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)