from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Post


urlpatterns = [
    path('', ListView.as_view(
        queryset = Post.objects.all().order_by("-date"),
        template_name = "home.html",
        paginate_by = 8), name = "home"),
    

    path('<int:pk>/<slug:slug>/', DetailView.as_view(
        model = Post,
        template_name = "post_singolo.html",), name = "singolo"),

    path('contatti/', views.contatti, name='contatti'),
    path('chi-sono/', views.chi_sono, name='chi-sono')
]

