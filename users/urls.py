from django.urls import path
from. import views
urlpatterns=[
    path("",views.welcome,name="welcome"),
    path("signup/",views.index, name="index"),
    path("login/",views.login, name="login"),
    path('home/@<username>',views.home, name='home'),
    path('@<username>',views.profile,name="profile"),
]