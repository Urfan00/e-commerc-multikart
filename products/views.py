from django.shortcuts import render, redirect
from django.db.models import Avg, Q
from products.forms import ReviewForm
from products.models import Brand, Category, Color, Image, ProductReview, ProductVersion, Products, Size
from django.views.generic import ListView, DetailView, CreateView



class ProductListView(ListView):
    model = Products
    template_name = 'category-page.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['colors'] = Color.objects.all()
        context['productcount'] = Products.objects.count()
        if Brand.objects.filter(category_id__category_name=self.request.GET.get('category')).all():
            context['brands'] = Brand.objects.filter(category_id__category_name=self.request.GET.get('category')).all()
        else:
            context['brands'] = Brand.objects.filter(category_id__category_name= 'Fashion').all()
        if self.request.GET.get('category') == 'Shoes':
            context['sizes'] = Size.objects.all()[4:]
        else:
            context['sizes'] = Size.objects.all()[:4]
        if ProductVersion.objects.filter(product_id__category_id__category_name=self.request.GET.get('category')).order_by("-created_at").all():
            context['new_products'] = ProductVersion.objects.filter(product_id__category_id__category_name=self.request.GET.get('category')).order_by("-created_at").all()[:3]
            context['new_products2'] = ProductVersion.objects.filter(product_id__category_id__category_name=self.request.GET.get('category')).order_by("-created_at").all()[3:6]
        else:
            context['new_products'] = ProductVersion.objects.filter(product_id__category_id__category_name='Fashion').order_by("-created_at").all()[:3]
            context['new_products2'] = ProductVersion.objects.filter(product_id__category_id__category_name='Fashion').order_by("-created_at").all()[3:6]
        return context

    def get_queryset(self):
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        color= self.request.GET.get('color')
        size= self.request.GET.get('size')
        minPrice= self.request.GET.get('minPrice')
        maxPrice= self.request.GET.get('maxPrice')

        if (category and brand):
            self.queryset = ProductVersion.objects.filter(product_id__category_id__category_name=category).all()
            self.queryset = ProductVersion.objects.filter(product_id__brand_id__name=brand).all()
        elif category:
            self.queryset = ProductVersion.objects.filter(product_id__category_id__category_name=category).all()
        elif brand:
            self.queryset = ProductVersion.objects.filter(product_id__brand_id__name=brand).all()
        elif size:
            self.queryset = ProductVersion.objects.filter(size_id__name=size).all()
        elif color:
            self.queryset = ProductVersion.objects.filter(color_id__name=color).all()
        else:
            self.queryset = ProductVersion.objects.all()
        return self.queryset


class ProductDetailView(DetailView, CreateView):
    model = Products
    template_name = 'product-page.html'
    form_class = ReviewForm
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        product_stats = ProductVersion.objects.get(product_id=self.object)
        product_stats.read_count += 1
        product_stats.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['images'] = Image.objects.all()
        context['colors'] = Color.objects.all()
        context['sizes'] = Size.objects.all()
        context['average'] = ProductReview.objects.filter(product_id__product_id__slug = self.kwargs.get('slug')).aggregate(average=Avg('product_rate'))
        context['reviews'] = ProductReview.objects.filter(product_id__product_id__slug = self.kwargs.get('slug')).all()[:3]
        context['new_products'] = ProductVersion.objects.filter(product_id__category_id__category_name = self.object.category_id).order_by("-created_at").all()[:3]
        context['new_products2'] = ProductVersion.objects.filter(product_id__category_id__category_name = self.object.category_id).order_by("-created_at").all()[3:6]
        context['related'] = ProductVersion.objects.filter(product_id__brand_id = self.object.brand_id).exclude(product_id__slug = self.kwargs.get('slug'))[:6]
        return context


    def form_valid(self, form, *args, **kwargs):
        form.instance.product_id = ProductVersion.objects.get(product_id__slug = self.kwargs.get('slug'))
        form.instance.save()
        self.object = self.get_object()
        product = ProductVersion.objects.get(product_id=self.object)
        product.review_count += 1
        rate = ProductReview.objects.filter(product_id__product_id__slug = self.kwargs.get('slug')).aggregate(average=Avg('product_rate'))
        product.rate_avg = rate['average']
        product.save()
        return redirect("product_detail", slug = self.kwargs.get('slug'))


class SearchResultsView(ListView):
    model = Products
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            products=ProductVersion.objects.filter(Q(product_id__product_name__icontains=query))[:6]
        else:
            products=ProductVersion.objects.all()[:6]
        return products


def vendorprofile(request):
    return render(request, 'vendor-profile.html')
