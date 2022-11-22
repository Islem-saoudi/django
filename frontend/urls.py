from urllib.parse import urlparse
from django.urls import path
from frontend import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug>/', views.DetailsBlogView.as_view(), name='blog-detail'),
    path('design/', views.DesignView.as_view(), name='design'),
    path('web/', views.WebView.as_view(), name='web'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('seo/', views.SeoView.as_view(), name='seo'),
    path('marketing/', views.MarketingView.as_view(), name='marketing'),
    path('what_we_do/', views.ServicesView.as_view(), name='services'),
    
]
