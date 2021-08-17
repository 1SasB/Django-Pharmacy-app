from django.urls import path, reverse_lazy
from .import views 

app_name='pharm'

urlpatterns = [
    path('', views.HomeView.as_view(),name='home'),
    path('home',views.HomeView.as_view(),name='home')


]