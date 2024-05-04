from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, Page
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, LoginForm, FilterByPrice, FilterByBrand, ChangeLoginForm
from .models import Brand, Category, ProductType, Article, Product, Basket, Order, Reviews


def get_home_page(request):
    return redirect('home')


def get_main_page(request):
    products = Product.objects.all().select_related('product_type', 'manufacturer', 'product_category',
                                                    'other_images', 'product_properties')
    categories = Category.objects.all()
    reviews = Reviews.objects.all()
    articles = Article.objects.all()
    products_by_rating = products.order_by('product_properties__rating')
    products_by_date = products.order_by('-product_properties__pub_date')
    brands = Brand.objects.all()
    if request.method == 'GET':
        if request.GET.get('search'):
            prod_unsort = Product.objects.filter(product_name__icontains=request.GET.get('search'))
            context = {'prod_unsort': prod_unsort}
            return render(request, 'search.html', context)
    context = {'categories': categories, 'products_by_rating': products_by_rating, 'articles': articles,
               'products_by_date': products_by_date, 'brands': brands, 'reviews': reviews}
    return render(request, 'home.html', context)


def register_user(request):
    form = UserRegistrationForm()
    error = ''
    if request.method == 'POST':
        a = UserRegistrationForm(request.POST)
        if a.is_valid():
            if a.cleaned_data.get('password') == a.cleaned_data.get('password2'):
                print(a.cleaned_data)
                b = User(username=a.cleaned_data.get('username'))
                b.set_password(a.cleaned_data.get('password'))
                print(b)
                b.save()
                return redirect('login')
            else:
                error = 'Пароли не совпадают'
                print('else')
        else:
            error = 'Форма не валидна'
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'register.html', context)


def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        a = LoginForm(request.POST)

        if a.is_valid():
            b = authenticate(username=a.cleaned_data.get('username'),
                             password=a.cleaned_data.get('password'))
            if b is not None:
                login(request, b)
                print('exist')
                return redirect('home')
            else:
                print('not exist')
                return HttpResponse('<a href="http://127.0.0.1:8000/home/" style="color: red; font-size: 25px;">'
                                    '<p>Неверный логин или пароль, продолжить<p></a>')
        else:
            print('not valid')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return redirect('home')


def get_user(request):
    print(request.headers)
    print(request.body)
    current_user = request.user
    order_history = Basket.objects.filter(user_name=current_user, is_complete=1)
    change_form = ChangeLoginForm()
    error = 'Введите данные'
    if request.method == 'POST':
        print(request.POST)
        new_data = ChangeLoginForm(request.POST)
        if request.POST.get('new_login') and request.POST.get('new_password') and request.POST.get('new_password2'):
            if new_data.is_valid():
                if new_data.cleaned_data.get('new_password') == new_data.cleaned_data.get('new_password2'):
                    current_user.username = (new_data.cleaned_data.get('new_login'))
                    current_user.set_password(new_data.cleaned_data.get('new_password'))
                    current_user.save()
                    error = 'Успешно изменено'
                else:
                    error = 'Пароли не совпадают'
        if request.POST.get('new_password') and request.POST.get('new_password2'):
            if new_data.is_valid():
                if new_data.cleaned_data.get('new_password') == new_data.cleaned_data.get('new_password2'):
                    current_user.set_password(new_data.cleaned_data.get('new_password'))
                    current_user.save()
                    error = 'Успешно изменено'
                else:
                    error = 'Пароли не совпадают'
    context = {'current_user': current_user, 'order_history': order_history, 'change_form': change_form, 'error': error}
    return render(request, 'user.html', context)


def get_catalog(request):
    prod_unsort = Product.objects.all().select_related('product_type', 'manufacturer', 'product_category',
                                                       'other_images', 'product_properties')
    products_by_rating = prod_unsort.order_by('product_properties__rating')
    paginator = Paginator(prod_unsort, 3)
    page_number = request.GET.get('page')
    prod_unsort = paginator.get_page(page_number)
    categories = Category.objects.all()
    product_types = ProductType.objects.all()
    brands = Brand.objects.all()
    articles = Article.objects.all()
    price_form = FilterByPrice()
    brand_form = FilterByBrand()
    if request.method == 'GET':
        print(request.GET)
        if request.GET.get('type_p') and request.GET.get('brand_1'):
            prod_unsort = Product.objects.filter(product_type=request.GET.get('type_p'),
                                                 manufacturer__in=request.GET.get('brand_1'))
        elif request.GET.get('type_p'):
            prod_unsort = Product.objects.filter(product_type=request.GET.get('type_p'))
        elif request.GET.get('brand_1'):
            prod_unsort = Product.objects.filter(manufacturer__in=request.GET.getlist('brand_1'))
            print(prod_unsort)
        elif request.GET.get('choice_form'):
            price_done = FilterByPrice(request.GET)
            if price_done.is_valid():
                prod_unsort = Product.objects.order_by(price_done.cleaned_data.get('choice_form'))
        elif request.GET.get('brand_form'):
            brand_done = FilterByBrand(request.GET)
            if brand_done.is_valid():
                print(brand_done.cleaned_data)
                prod_unsort = Product.objects.filter(manufacturer__in=brand_done.cleaned_data.get('brand_form'))
        elif request.GET.get('search'):
            prod_unsort = Product.objects.filter(product_name__icontains=request.GET.get('search'))
        elif request.GET.get('sort_by'):
            prod_unsort = Product.objects.filter()
    context = {'prod_unsort': prod_unsort, 'categories': categories, 'product_types': product_types, 'articles': articles,
               'brands': brands, 'price_form': price_form, 'brand_form': brand_form, 'products_by_rating': products_by_rating}
    return render(request, 'catalog.html', context)


def get_catalog_by_category(request, category):
    prod_category = Product.objects.filter(product_category=category)
    categories = Category.objects.all()
    cat_selected = Category.objects.get(id=category)
    articles = Article.objects.all()
    products_by_rating = Product.objects.order_by('product_properties__rating')
    price_form = FilterByPrice()
    brand_form = FilterByBrand()
    if request.method == 'GET':
        if request.GET.get('choice_form'):
            price_done = FilterByPrice(request.GET)
            if price_done.is_valid():
                prod_category = Product.objects.order_by(price_done.cleaned_data.get('choice_form'))
        if request.GET.get('brand_form'):
            brand_done = FilterByBrand(request.GET)
            if brand_done.is_valid():
                prod_category = Product.objects.filter(manufacturer__in=brand_done.cleaned_data.get('brand_form'),
                                                       product_category=category)
    context = {'prod_category': prod_category, 'category': category, 'categories': categories, 'articles': articles,
               'cat_selected': cat_selected, 'price_form': price_form,
               'brand_form': brand_form, 'products_by_rating': products_by_rating}
    return render(request, 'catalog_by_category.html', context)


def get_card_product(request, product_id, product_amount):
    products = Product.objects.all().select_related('product_type', 'manufacturer', 'product_category',
                                                    'other_images', 'product_properties')
    item_1 = products.get(id=product_id)
    item_2 = Article.objects.all()
    same_products = Product.objects.filter(product_name=item_1.product_name)
    sorted_by_rating = Product.objects.order_by('product_properties__rating')
    if request.method == 'GET':
        print(request.GET)
        if request.GET.get('search'):
            prod_unsort = Product.objects.filter(product_name__icontains=request.GET.get('search'))
            context = {'prod_unsort': prod_unsort}
            return render(request, 'search.html', context)
        if request.GET.get('by_brand'):
            prod_unsort = Product.objects.filter(manufacturer=item_1.manufacturer)
            context = {'prod_unsort': prod_unsort}
            return render(request, 'search.html', context)
    context = {'item_1': item_1, 'item_2': item_2, 'product_amount': product_amount,
               'sorted_by_rating': sorted_by_rating, 'same_products': same_products}
    return render(request, 'card_product.html', context)


def get_card_increase(request, product_id, product_amount):
    product = Product.objects.get(id=product_id)
    product_amount = int(product_amount)
    product_amount += 1
    print(product_amount)
    return redirect('card_product', product_id, product_amount)


def get_card_decrease(request, product_id, product_amount):
    product = Product.objects.get(id=product_id)
    product_amount = int(product_amount)
    if product_amount > 1:
        product_amount -= 1
    return redirect('card_product', product_id, product_amount)


def get_brands(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'brands.html', context)


def get_articles(request):
    items = Article.objects.all()
    sorted_by_rating = Product.objects.order_by('product_properties__rating')
    if request.method == 'GET':
        if request.GET.get('search'):
            prod_unsort = Product.objects.filter(product_name__icontains=request.GET.get('search'))
            context = {'prod_unsort': prod_unsort}
            return render(request, 'search.html', context)
    context = {'items': items, 'sorted_by_rating': sorted_by_rating}
    return render(request, 'articles.html', context)


def get_article_self(request, article_name):
    items = Article.objects.get(article_name=article_name)
    sorted_by_rating = Product.objects.order_by('product_properties__rating')
    if request.method == 'GET':
        if request.GET.get('search'):
            prod_unsort = Product.objects.filter(product_name__icontains=request.GET.get('search'))
            context = {'prod_unsort': prod_unsort}
            return render(request, 'search.html', context)
    context = {'items': items, 'sorted_by_rating': sorted_by_rating}
    return render(request, 'article_self.html', context)


def get_basket(request):
    current_user = request.user
    products = Product.objects.all().select_related('product_type', 'manufacturer', 'product_category',
                                                    'other_images', 'product_properties')
    baskets = Basket.objects.filter(user_name=current_user, is_complete=0)
    articles = Article.objects.all()
    products_by_rating = products.order_by('product_properties__rating')
    products_by_date = products.order_by('-product_properties__pub_date')
    total_price = 0
    total_amount = 0
    for i in baskets:
        i.cost = i.amount * i.product.product_properties.price
        total_price += i.cost
        total_amount += i.amount
    context = {'baskets': baskets, 'total_price': total_price, 'total_amount': total_amount, 'articles': articles,
               'products_by_rating': products_by_rating, 'products_by_date': products_by_date}
    return render(request, 'basket.html', context)


def add_to_basket(request, product_id, product_amount):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user_name=request.user, product=product_id, is_complete=0)
    basket = baskets.first()
    if not baskets:
        Basket.objects.create(user_name=request.user, product=product, amount=product_amount,
                              cost=product.product_properties.price, is_complete=0)
        product.product_properties.rating += product_amount
        product.save()
    else:
        basket.amount += 1
        product.product_properties.rating += 1
        basket.save()
        product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_increase(request, product_id):
    basket = Basket.objects.get(product_id=product_id, is_complete=0)
    product = Product.objects.get(id=product_id)
    basket.amount += 1
    product.product_properties.rating += 1
    basket.save()
    product.save()
    return redirect('basket')


def get_decrease(request, product_id):
    basket = Basket.objects.get(product_id=product_id, is_complete=0)
    product = Product.objects.get(id=product_id)
    if basket.amount > 1:
        basket.amount -= 1
        product.product_properties.rating -= 1
        basket.save()
        product.save()
    else:
        product.product_properties.rating -= 1
        product.save()
        basket.delete()
    return redirect('basket')


def get_remove(request, product_id):
    basket = Basket.objects.get(product_id=product_id, is_complete=0)
    product = Product.objects.get(id=product_id)
    product.product_properties.rating -= basket.amount
    product.save()
    print(basket)
    basket.delete()

    return redirect('basket')


def get_order_create(request, total_price, total_amount):
    if total_amount == 0:
        return redirect('empty_basket')
    current_user = request.user
    basket_items = Basket.objects.filter(user_name=current_user, is_complete=False)
    print(basket_items)
    if request.method == 'POST':
        print(request.POST)
        print(basket_items)
        for i in basket_items:
            order_complete = Order(user_name=current_user,
                                   user_voiced_name=request.POST.get('client_name'),
                                   user_tel=request.POST.get('client_tel'),
                                   total_order_price=total_price,
                                   order_compound=i)
            print(order_complete)
            i.is_complete = True
            i.save()
            order_complete.save()
        return redirect('order_complete')
    context = {'total_price': total_price, 'total_amount': total_amount}
    return render(request, 'order_create.html', context)


def get_order_complete(request):
    return render(request, 'order_complete.html')


def get_empty_basket(request):
    return render(request, 'empty_basket.html')


def get_service(request):
    return render(request, 'service.html')
