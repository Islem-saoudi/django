from django.shortcuts import render

def page_not_found_view(request, exception):
    template_name= 'api/404.html'
    return render(request, template_name, status='404')


def error_view(request):
    template_name='api/500.html'
    return render(request, template_name, status='500')

def permission_denied_view(request, exception):
    template_name='api/403.html'
    return render(request, template_name, status='403')

def bad_request_view(request, exception):
    template_name='api/400.html'
    return render(request, template_name, status='400')

