from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Employees, Faq, Instagram, Logo, OurTeam
from .forms import ContactFormModel
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instalogos'] = Instagram.objects.all()
        context['logos'] = Logo.objects.all()
        return context


class AboutListView(ListView):
    model = OurTeam
    template_name = 'about-page.html'
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employees.objects.all()
        return context


class CreateContactView(LoginRequiredMixin, CreateView):
    template_name = 'contact.html'
    form_class = ContactFormModel
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your comment has been sent successfully!')
        return redirect('contact')


class Faq(ListView):
    template_name = 'faq.html'
    model = Faq
    context_object_name = 'faqs'


def error(request):
    return render(request, '404.html')
