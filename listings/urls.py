from django.urls import path

from . import views

# app_name = 'listings'

urlpatterns = [
    path("", views.index, name="index"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    # path('package/<int:pk>', views.package_detail_view, name='package-detail'),
    # path('package/create/', views.PackageCreate.as_view(), name='package-create'),
    path('post/create/', views.post_create, name='post-create'),
    # path('package/<int:pk>/update/', views.PackageUpdate.as_view(), name='package-update'),
    # path('package/<int:pk>/delete/', views.PackageDelete.as_view(), name='package-delete'),
    # path("privacy", views.privacy, name="privacy"),
    # path("app-ads.txt", views.appads, name="appads"),
]