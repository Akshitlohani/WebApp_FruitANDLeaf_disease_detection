from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('disease_encyclopedia_papaya/', views.diseases_papaya, name = "diseases_papaya"),
    path('disease_encyclopedia_tomato/', views.diseases_tomato, name = "diseases_tomato"),
    path('disease_encyclopedia_orange/', views.diseases_orange, name = "diseases_orange"),
    path('disease_encyclopedia_dragonfruit/', views.diseases_dragonfruit, name = "diseases_dragonfruit"),
    path('disease_encyclopedia_pomegranate/', views.diseases_pomegranate, name = "diseases_pomegranate"),
    
    path('disease_detection_papaya/', views.detection_papaya, name = "detection_papaya"),
    path('disease_detection_tomato/', views.detection_tomato, name = "detection_tomato"),
    path('disease_detection_orange/', views.detection_orange, name = "detection_orange"),
    path('disease_detection_dragonfruit/', views.detection_dragonfruit, name = "detection_dragonfruit"),
    path('disease_detection_pomegranate/', views.detection_pomegranate, name = "detection_pomegranate"),
    
    path('login/', views.login_page, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('signup/', views.signup_page, name = "signup"),
]
handler404 = 'fruit_disease_detection_app.views.handler404'