from django.urls import path, re_path

from .views import *
urlpatterns = [
    path('/', uni_main),
    path('/index/', uni_index, name= 'index'),
    path('/<int:id>', uni_detail, name= 'detail'),
    path('/create/', uni_create, name= 'create'),
    path('/<int:id>/update/', uni_update, name= 'update'),
    path('/<int:id>/delete/', uni_delete, name= 'delete'),

]