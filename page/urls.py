from django.urls import path
from page import views

urlpatterns = [
    path("myspace/page/add/", views.AddPageView.as_view(), name="add-page"),
    path("myspace/page/list/", views.ListPageView.as_view(), name="list-page"),
    path("myspace/page/update/<slug>/", views.UpdatePageView.as_view(), name="update-page"),
    path("<slug>/", views.DetailPageView.as_view(), name="detail_page"),

]