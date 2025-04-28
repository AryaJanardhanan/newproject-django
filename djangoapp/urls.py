from django.urls import path
from .import views as v

urlpatterns = [
    path('',v.home, name='home'),
    path('about/',v.about, name='about'),
    path('base/',v.base, name='base'),
    path('index/',v.index, name='index'),
    path('contact/',v.contact, name='contact'),
    path('student/', v.students, name='student'),
    path('newstu/', v.newstu, name='studt'),
    path('register/', v.register, name='register'),
    path('signin/', v.signin, name='signin'),
    path('logout/', v.uslogout, name='logout'),
    path('list/', v.stlist, name='list'),
    path('item/<int:pk>/delete/', v.delt, name='delete'),
    path('item/<int:pk>/edit/', v.editt, name='edit'),   
    
]