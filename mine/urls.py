from django.urls import path
from . import views

app_name = 'cargo'
urlpatterns = [
    path('', views.index, name='index'),
    path('cargo/<int:cargo_id>/', views.detail, name='detail'),
    # path('cargo/<int:cargo_id>/results/', views.results, name='results'),
    path('cargo/<int:cargo_id>/calc/', views.calc, name='calc'),
]
