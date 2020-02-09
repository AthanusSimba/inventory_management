from django.conf.urls import  url
from django.urls import path
from .views import index,\
    display_laptops,\
    display_desktops,\
    display_mobiles,\
    add_laptop,\
    add_desktop,\
    add_mobile,\
    edit_laptop,\
    edit_desktop,\
    edit_mobile,\
    delete_laptop,\
    delete_desktop,\
    delete_mobile
urlpatterns = [
    path('', index, name='index'),
    path('display_laptop/', display_laptops, name='display_laptop'),
    path('display_desktop/', display_desktops, name='display_desktop'),
    path('display_mobile/', display_mobiles, name='display_mobile'),
    path('add_laptop/', add_laptop, name='add_laptop'),
    path('add_desktop/', add_desktop, name='add_desktop'),
    path('add_mobile/', add_mobile, name='add_mobile'),

    path('edit_laptop/(?P<pk>)', edit_laptop, name='edit_laptop'),
    path('edit_desktop/(?P<pk>)', edit_desktop, name='edit_desktop'),
    path('edit_mobile/(?P<pk>)', edit_mobile, name='edit_mobile'),

    path('delete_laptop/(?P<pk>)', delete_laptop, name='delete_laptop'),
    path('delete_desktop/(?P<pk>)', delete_desktop, name='delete_desktop'),
    path('delete_mobile/(?P<pk>)', delete_mobile, name='delete_mobile'),

]