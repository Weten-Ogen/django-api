from django.urls import path
from . import views

urlpatterns = [
   path('', views.ProductCreateApiView.as_view()),
   path('list/', views.ProductListApiView.as_view()),
   path('<int:pk>/',views.ProductDetailApiView.as_view()),
   path('<int:pk>/delete/',views.ProductDeleteApiView.as_view()),
   path('<int:pk>/update/',views.ProductUpdateApiView.as_view()),
]