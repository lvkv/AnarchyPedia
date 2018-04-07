from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    path('wiki/<title>', views.get_article),
    path('wiki/<title>/edit', views.edit_article)
]