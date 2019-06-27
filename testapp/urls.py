from django.urls import path
# from testapp.views import PrintHello # importing one by one
from testapp import views  # importing all views from testapp
# from testapp.views import *
from django.contrib.auth import views as auth_views

app_name = 'testapp' # url namespacing
urlpatterns = [
    path('',views.PrintHello,name='testpage'),
    path('register/',views.register,name='register'),
    path('add_laptop/',views.save_laptop, name='add_laptop'),
    path('retrieve/',views.retrieve_data, name='retrieve'),
    path('update/<int:id>/',views.update_data, name='update'),
    path('delete/<int:id>/',views.delete_date, name='delete'),
    path('save/',views.save_with_html, name='save'),

]