# pylint: disable=missing-module-docstring
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm, CategoryForm


def all_products(request):
    """
    A view to show all products, including sorting and search categories
    """

    products = Product.objects.all()
    query = None
    search_categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            search_categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=search_categories)
            search_categories = Category.objects.filter(name__in=search_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter a search criteria')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': search_categories,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """
    A view to show an individual product
    """

    product = get_object_or_404(Product, pk=product_id)

    # if request.GET:
    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def categories(request):
    """
    display and add a category in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))

    categories = Category.objects.all()
    form = CategoryForm()
    template = 'products/categories.html'
    context = {
        'categories': categories,
        'form': form
    }

    return render(request, template, context)


@login_required
def add_category(request):
    """
    display and add a category in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('categories'))
        else:
            messages.error(request, 'Failed to add category. Please ensure the form is valid.')
    else:
        form = CategoryForm()
    template = 'products/categories.html'
    context = {
        'categories': categories,
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    """
    Edit a category in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated category!')
            return redirect('categories')
        else:
            messages.error(request, 'Failed to update category. Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.name}')

    template = 'products/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)

@login_required
def delete_category(request, category_id):
    """
    Delete a category from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category deleted!')
    return redirect(reverse('categories'))
