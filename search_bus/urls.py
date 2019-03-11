from django.urls import path
from . import views

# 正在部署的应用的名称
app_name = 'search_bus'
urlpatterns = [
    path('search_bus/', views.search, name='search'),
    path('reverse/', views.reverse, name='reverse'),
    path('', views.welcome, name='welcome')
]
