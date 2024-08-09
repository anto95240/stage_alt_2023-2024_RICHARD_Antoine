from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.role_login, name='role_login'),
    path('<str:role>/register/', views.role_register, name='role_register'),
    path('logout/', views.logout_view, name='logout'),

    path('user-info/<int:user_id>/', views.user_info, name='user_info'),
    path('user-update/<int:user_id>/', views.user_update, name='user-update'),
]
