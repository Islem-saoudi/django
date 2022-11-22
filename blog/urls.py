from django.urls import path
from blog import views

urlpatterns = [
    path("myspace/blog/add/", views.AddPostView.as_view(), name="add-post"),
    path("myspace/blog/list/", views.ListPostView.as_view(), name="blog-list"),
    path("myspace/blog/update/<slug>/", views.UpdatePostView.as_view(), name="update-post"),
    path("myspace/blog/delete/<slug>/", views.DeletePostView.as_view(), name="delete-post"),
    path("myspace/blog/categories/",views.AddCategoryView.as_view(), name="categories"),
    path("myspace/blog/categories/update/<slug>/", views.UpdateCategoryView.as_view(), name="update-category"),
    path("myspace/blog/category/delete/<slug>/", views.DeleteCategoryView.as_view(), name="delete-category"),

]