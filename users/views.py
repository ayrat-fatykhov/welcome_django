import string
import random

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from users.forms import UserRegisterForm, UserPasswordRecoveryForm
from users.models import User


class RegisterView(CreateView):
    """
    Реализует возможность регистрации нового пользователя
    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Отправляет на почту пользователя письмо о верификации
        """
        new_user = form.save()
        current_site = self.request.get_host()
        ver_code = "".join([str(random.randint(1, 9)) for i in range(5)])
        new_user.ver_code = ver_code
        new_user.is_active = False
        new_user.save()
        send_mail(
            subject='Верификация',
            message=f'Ваш код: {ver_code}.\nПерейдите по ссылке: {current_site}/users/emailconfirm',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class EmailConfirmView(TemplateView):
    """
    Реализует возможность верификации пользователя по коду
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'users/email_confirm.html')

    def post(self, request, *args, **kwargs):
        code = request.POST.get('ver_code')
        user = get_object_or_404(User, ver_code=code)

        if not user.is_active:
            user.is_active = True
            user.save()
            return redirect('users:login')
        return redirect('product_list')


class UserPasswordRecoveryView(FormView):
    """
    Реализует возможность восстановления пароля
    """
    template_name = 'users/user_password_reset.html'
    form_class = UserPasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """
        Отправляет на почту новый пароль для входа на платформу
        """
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()

        if user is not None:
            characters = string.ascii_letters + string.digits
            new_password = ''.join(random.choice(characters) for i in range(12))

            user.password = make_password(new_password)
            user.save()

            subject = 'Восстановление пароля'
            message = f'Ваш новый пароль: {new_password}'
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

        return super().form_valid(form)
