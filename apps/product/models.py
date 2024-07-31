from django.db import models
from django_jalali.db import models as jmodels
from django.shortcuts import reverse
from apps.user.models import UserModel
from django.core.validators import MaxValueValidator, MinValueValidator


# This Model is main category for all products and child categories base parent
class MainCategoryModel(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    url = models.SlugField(unique=True, allow_unicode=True, verbose_name='لینک')
    active = models.BooleanField(default=True, verbose_name='فعال')
    image = models.ImageField(upload_to='product/category', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:products_main_category', args=[self.url])


# This Model is child category and this models each category can be a parent from child category
class ChildCategoryModel(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    url = models.SlugField(unique=True, allow_unicode=True, verbose_name='لینک')
    base_category = models.ForeignKey(to=MainCategoryModel, on_delete=models.CASCADE,
                                      related_name='base_category_child', verbose_name='دسته بندی اصلی')
    parent_category = models.ForeignKey(to='ChildCategoryModel', on_delete=models.CASCADE,
                                        related_name='child_category', null=True, blank=True,
                                        verbose_name='دسته بندی پدر')
    active = models.BooleanField(default=True, verbose_name='فعال')
    image = models.ImageField(upload_to='product/category', verbose_name='')
    description = models.TextField(verbose_name='', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:products_child_category', args=[self.url])


class BrandModel(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    image = models.ImageField(upload_to='product/brands_image', verbose_name='تصویر')
    url = models.SlugField(unique=True, allow_unicode=True, verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')
    active = models.BooleanField(default=True, verbose_name='فعال')
    category = models.ManyToManyField(ChildCategoryModel, related_name='category_brands', verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class ProductPriceChartModel(models.Model):
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, related_name='product_price_chart',
                                verbose_name='کالا')
    price = models.IntegerField(verbose_name='قیمت')
    date = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ')


class ProductModel(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    main_category = models.ForeignKey(to=MainCategoryModel, on_delete=models.DO_NOTHING,
                                      related_name='main_category_products', verbose_name='دسته بندی اصلی')
    child_category = models.ForeignKey(to=ChildCategoryModel, on_delete=models.DO_NOTHING,
                                       related_name='child_category_products', verbose_name='دسته بندی فرزند')
    brand = models.ForeignKey(to=BrandModel, on_delete=models.DO_NOTHING, related_name='brands_products',
                              verbose_name='برند')
    description = models.TextField(verbose_name='توضیحات')
    url = models.SlugField(unique=True, allow_unicode=True, verbose_name='لینک')
    image = models.ImageField(upload_to='product/product_images', verbose_name='تصویر')
    published_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    update_date = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    price_after_off = models.PositiveIntegerField(null=True, blank=True, verbose_name='قیمت بعد از تخفیف')
    view_num = models.PositiveIntegerField(verbose_name='تعداد بازدید')
    off = models.PositiveIntegerField(default=0, verbose_name='تخفیف')
    sell = models.PositiveIntegerField(default=0, verbose_name='تعداد فروش')
    active = models.BooleanField(default=False, verbose_name='فعال')
    available = models.BooleanField(default=True, verbose_name='موجودی')

    def get_absolute_url(self):
        return reverse('product:product_detail_view', args=[self.url])

    def save(self, *args, **kwargs):
        self.price_after_off = self.price * (100 - self.off) / 100
        super().save(*args, **kwargs)
        ProductPriceChartModel.objects.get_or_create(product_id=self.id, price=self.price_after_off)

    def __str__(self):
        return self.title


class CategoryFiledModel(models.Model):
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    category = models.ManyToManyField(to=ChildCategoryModel, related_name='child_category_field',
                                      verbose_name='دسته بندی')

    def __str__(self):
        return self.title


class ProductFieldModel(models.Model):
    field = models.ForeignKey(to=CategoryFiledModel, on_delete=models.CASCADE, related_name='category_fields',
                              verbose_name='فیلد')
    product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE, related_name='product_fields',
                                verbose_name='کالا')
    amount = models.TextField(verbose_name='مقدار')


class ProductImageModel(models.Model):
    product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE, related_name='product_images',
                                verbose_name='کالا')
    image = models.ImageField(upload_to='product/product_images', verbose_name='تصویر')


class ProductVideoModel(models.Model):
    product = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE, related_name='product_video',
                                verbose_name='کالا')
    video = models.ImageField(upload_to='product/product_videos', verbose_name='ویدیو')


class ProductCommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_product_comments',
                             verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_comments',
                                verbose_name='کالا')
    text = models.TextField(verbose_name='متن')
    published_date = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    edit_date = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    active = models.BooleanField(default=False, verbose_name='وضعیت')
    admin_seen = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='admin_seen_product_comments',
                                   null=True, blank=True, verbose_name='بررسی ادمین')
    admin_solve = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='admin_solve_product_comments',
                                    null=True, blank=True)
    admin_solve_text = models.TextField(null=True, blank=True)
    grade = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    like_num = models.PositiveIntegerField(default=0)
    dislike_num = models.PositiveIntegerField(default=0)


class ProductCommentPositivePointsView(models.Model):
    comment = models.OneToOneField(ProductCommentModel, on_delete=models.CASCADE,
                                   related_name='comment_positive_points')
    text = models.TextField()

    def get_list(self):
        return self.text.split(',')


class ProductCommentNegativePointsView(models.Model):
    comment = models.OneToOneField(ProductCommentModel, on_delete=models.CASCADE,
                                   related_name='comment_negative_points')
    text = models.TextField()

    def get_list(self):
        return self.text.split(',')


class UserFavoriteProductModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_favorite_product',
                             verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='favorite_product',
                                verbose_name='کالا')


class ProductViewModel(models.Model):
    ip = models.CharField(max_length=100, verbose_name='ای پی')
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_product_view', null=True,
                             blank=True, verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product_view',
                                verbose_name='محصول')
    date_view = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ بازدید')