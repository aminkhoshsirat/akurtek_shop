from django.shortcuts import render
from django.views.generic import View
from apps.panel import SiteDetailModel


class HeaderView(View):
    def get(self, request):
        context = {
            'site_detail': SiteDetailModel.objects.first()
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