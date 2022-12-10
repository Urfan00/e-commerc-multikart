from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify



class Category(models.Model):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Color(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name} color"


class Size(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name} size"


class Brand(models.Model):
    name = models.CharField(max_length= 50)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='brand_category')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class Products(models.Model):
    discounts = (
        (5, '5'),
        (10, '10'),
        (15, '15'),
        (20, '20'),
        (25, '25'),
        (30, '30'),
        (35, '35'),
        (40, '40'),
        (45, '45'),
        (50, '50')
    )
    product_name = models.CharField(max_length = 50)
    product_details = models.TextField()
    short_description = models.TextField()
    long_description = models.TextField()
    in_sale = models.BooleanField(default=False)
    price = models.FloatField()
    new_price = models.FloatField(null=True, blank=True)
    discount = models.IntegerField(choices=discounts, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="product_images")
    brand_id = models.ForeignKey(Brand, on_delete = models.CASCADE, related_name='brand')
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='product_category')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        if self.in_sale:
            self.new_price = self.price - self.price*(self.discount/100)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductVersion(models.Model):
    quantity = models.PositiveIntegerField()
    rate_avg = models.FloatField(default=0)
    review_count = models.PositiveIntegerField(default=0)
    read_count = models.PositiveIntegerField(default=0)
    size_id = models.ManyToManyField(Size, related_name="product_size")
    color_id = models.ManyToManyField(Color, related_name="product_color")
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_version")
    images_id = models.ManyToManyField(Image, related_name='images_of_products')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id.product_name}'s version"

    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"


class ProductReview(models.Model):
    Rates = {
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100")
    }
    product_rate = models.IntegerField(choices=Rates)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    review_title_1 = models.TextField()
    review_title_2 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    product_id = models.ForeignKey(ProductVersion, on_delete = models.CASCADE, related_name="product_review")
    
    def __str__(self):
        return f"{self.name}'s reviews"

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"
