from django.urls import path
from . import views

urlpatterns = [
    path('',views.userLogin, name="login" ),
    path('logout/',views.userLogout,name='logout'),
    path('home/',views.home, name="home" ),
    path('about/',views.about,name="about" ),
    path('register/',views.register,name="register" ),
    path('patient/', views.patient,name='patient'),
    path('patient/<int:id>/', views.patient,name='edite'),
    path('delete/<int:id>',views.deletpatient,name='deletpatient')
]