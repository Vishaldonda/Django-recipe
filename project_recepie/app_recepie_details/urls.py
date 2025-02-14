from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe_list/<int:recp_id>/',views.detail,name = 'detail')
]
