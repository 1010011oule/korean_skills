from django.urls import path
from training import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # This is the homepage
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('levels/', views.level_list, name='level_list'),  # Levels page
    path('levels/<int:level_number>/<str:section_type>/', views.section_detail, name='section_detail'),
    path('sections/<int:section_id>/exercises/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
]

