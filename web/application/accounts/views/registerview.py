from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = 'registration/user_form.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your registration was successfull')
            return HttpResponseRedirect(reverse('home'))
        else:
            return self.form_invalid(form)
