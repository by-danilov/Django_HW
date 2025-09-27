# users/views.py

from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from users.models import User
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            subject='Добро пожаловать!',
            message=f'Привет, {user.email}! Вы успешно зарегистрированы.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile.html'
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        return self.request.user
