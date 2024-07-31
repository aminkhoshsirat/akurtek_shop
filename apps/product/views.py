from django.shortcuts import render
from django.views.generic import View
from apps.panel.models import SiteDetailModel
from .models import *
from apps.blog.models import BlogCategoryModel


class HeaderView(View):
    def get(self, request):
        context = {
            'site_detail': SiteDetailModel.objects.first(),
            'categories': MainCategoryModel.objects.prefetch_related('base_category_child').filter(active=True),
            'blog_categories': BlogCategoryModel.objects.prefetch_related('category_child').filter(active=True,
                                                                                                   base=None),
        }
        return render(request, 'partial/header.html', context)


class FooterView(View):
    def get(self, request):
        context = {
            'site_detail': SiteDetailModel.objects.first()
        }
        return render(request, 'partial/footer.html', context)


class IndexView(View):
    def get(self, request):
        context = {

        }
        return render(request, 'index.html', context)