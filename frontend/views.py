import email
from multiprocessing import context
from django.shortcuts import render, redirect
from frontend.models import FrontendContact
from frontend.forms import FrontendContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from django.utils.translation import gettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from blog.models import Blog, Category


class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['article_list'] = Blog.objects.order_by('-CreatedDate')[:3]
        return context


class ContactView(SuccessMessageMixin, CreateView):
    model = FrontendContact
    form_class = FrontendContactForm
    success_message = _(
        "Your submission was successfully received, and our team will answer you as soon as possible")
    success_url = reverse_lazy("contact")
    template_name = 'frontend/contact.html'

    def form_valid(self, form, **kwargs):
        full_name = form.cleaned_data['Full_name']
        email = form.cleaned_data['Email']
        topic = form.cleaned_data['Topics']
        message = form.cleaned_data['Message']
        subject, from_email, to = topic, 'noreply@gisysco.com', "saoudisaoudi56@gmail.com"
        text_content = _('New email from contact gisysco.')
        html_content = _(
            f'Hello Team <br> <p>Mr/Ms: <strong>{full_name}</strong> need help about <strong> {topic} </strong> <br> His/Her message:<br> {message} </p> <p><a href="mailto:{email}">Reply to customer email</a></p>')
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super().form_valid(form)


class BlogView(ListView):
    model = Blog
    paginate_by = 10
    template_name = 'frontend/blog.html'

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        kwargs['articles_list'] = Blog.objects.order_by('-CreatedDate')[:6]

        return super(BlogView, self).get_context_data(**kwargs)


class DetailsBlogView(DetailView):
    model = Blog
    template_name = 'frontend/views/details_blog.html'

    def get_context_data(self, **kwargs):
        kwargs['cat_list'] = Category.objects.order_by('id')
        kwargs['articles_list'] = Blog.objects.order_by('-CreatedDate')[:6]

        return super(DetailsBlogView, self).get_context_data(**kwargs)


class DesignView(TemplateView):
    template_name = 'frontend/views/design.html'


class WebView(TemplateView):
    template_name = 'frontend/views/web_dev.html'


class MobileView(TemplateView):
    template_name = 'frontend/views/mobile_dev.html'


class SeoView(TemplateView):
    template_name = 'frontend/views/seo.html'


class MarketingView(TemplateView):
    template_name = 'frontend/views/marketing.html'


class ServicesView(TemplateView):
    template_name = 'frontend/views/services.html'
