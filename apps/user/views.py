from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, ListView
from apps.product.models import UserFavoriteProductModel, ProductCommentModel
from .models import UserAddressModel
from apps.payment.models import BuketModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from .forms import *
from utils import send_activation_code
from redis import Redis
from random import randint

re = Redis(host='localhost', port=6379, db=0)


class LoginPasswordView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel.objects.filter(phone=cd['phone']).first()
            if user:
                if user.ban:
                    return HttpResponse('کاربر مسدود شده است')
                else:
                    check = user.check_password(cd['password'])
                    if check:
                        login(request, user)
                        return redirect(request.META['HTTP_REFERER'])
                    else:
                        return HttpResponse('رمز عبور اشتباه است')
            else:
                return HttpResponse('کاربر یافت نشد')


class LoginSendActivationView(View):
    def post(self, request):
        form = LoginSendForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            user = UserModel.objects.filter(phone=phone).first()
            if user:
                if user.ban:
                    return HttpResponse('کاربر مسدود شده است')
                else:
                    time = re.ttl(f'user:activation:{user.phone}')
                    if time < 480:
                        code = randint(100000, 999999)
                        re.set(f'user:activation:{user.phone}', code, ex=10 * 60)
                        send_activation_code('کد فعال سازی ارسال شد')
                    else:
                        return HttpResponse('کد فعال سازی قبلا ارسال شده است')
            else:
                return HttpResponse('کاربر یافت شد')


class LoginActivationView(View):
    def post(self, request):
        form = LoginActivationForm(request.POST)
        if form.is_valid():
            cd =  form.cleaned_data
            user = UserModel.objects.filter(phone=cd['phone']).first()
            if user:
                if user.ban:
                    return HttpResponse('کاربر مسدود شده است')
                else:
                    code = re.get(f'user:activation:{user.phone}')
                    if code == cd['code']:
                        login(request, user)
                        return redirect(request.META['HTTP_REFERER'])
            else:
                return HttpResponse('کاربر یافت شد')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('product:index')


class AccountView(LoginRequiredMixin, ListView):
    template_name = 'user/account.html'
    model = UserFavoriteProductModel
    context_object_name = 'favorites'
    paginate_by = 20
    queryset = UserFavoriteProductModel.objects.filter(product__active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        addresses = UserAddressModel.objects.filter(user=user)
        context['addresses'] = addresses
        return context


class CommentsView(LoginRequiredMixin, ListView):
    template_name = 'user/comments.html'
    context_object_name = 'comments'
    model = ProductCommentModel
    paginate_by = 20

    def get_queryset(self):
        return ProductCommentModel.objects.filter(user=self.request.user)


class BucketView(LoginRequiredMixin, ListView):
    template_name = 'user/buckets.html'
    context_object_name = 'buckets'
    model = BuketModel
    paginate_by = 20

    def get_queryset(self):
        return BuketModel.objects.filter(user=self.request.user)


class UserEditView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm()
        context = {
            'form': form
        }
        return render(request, 'user/profile-edit.html', context)

    def post(self, request):
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponse('success')

        else:
            return HttpResponse('failed')
