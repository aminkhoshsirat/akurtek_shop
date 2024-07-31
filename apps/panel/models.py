from django.db import models
from apps.product.models import ProductModel


class SiteDetailModel(models.Model):
    title = models.CharField(max_length=10000)
    logo = models.ImageField(upload_to='site_detail/image')
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField()
    empty_cart_image = models.ImageField(upload_to='site_detail/image')
    footer_title = models.CharField(max_length=1000)
    footer_text = models.TextField()
    copy_right = models.TextField()
    enamad_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    enamad_url = models.URLField(null=True, blank=True)
    kasbokar_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    kasbokar_url = models.URLField(null=True, blank=True)
    samandehi_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    samandehi_url = models.URLField(null=True, blank=True)
    limit_of_address_can_add = models.IntegerField()
    suggested_products_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    amazing_products_image = models.ImageField(upload_to='site_detail/image', null=True, blank=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)


class AdvertisingBannerModel(models.Model):
    title = models.CharField(max_length=1000)
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE, related_name='banner_products')
    image = models.ImageField(upload_to='panel/banners')
    active = models.BooleanField(default=True)