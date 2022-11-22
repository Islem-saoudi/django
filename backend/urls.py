from urllib.parse import urlparse
from django.urls import path
from backend import views
urlpatterns = [
    path('myspace/', views.MySpaceViews.as_view(), name='dashboard'),
    path('history/', views.HistoryViews.as_view(), name='history'),
    path('profile/', views.ProfileViews.as_view(), name='profile'),
    path('marketing_form/', views.MarketingFormViews.as_view(), name='marketing_f'),
    path('marketing_list/', views.MarketingListViews.as_view(), name='marketing_l'),
    path('technical_form/', views.TechnicalFormViews.as_view(), name='technical_f'),
    path('technical_list/', views.TechnicalListViews.as_view(), name='technical_l'),
    path('add_update_tasks/', views.UpdateTasksViews.as_view(), name='update_t'),
    path('check_tasks/', views.CheckTasksViews.as_view(), name='check_t'),
]