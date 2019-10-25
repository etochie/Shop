from django.urls import path
from product import views

app_name = 'product'
urlpatterns = [
    path('<slug>/', views.product_detail, name='product_detail_url' )
]