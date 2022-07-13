from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateUserView, registration

app_name = 'user'
urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    # 使用內建login views 去呼叫模板
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    # 使用者申請表單頁面
    path('registration/', registration, name='registration'),
    # 使用者完成表單頁面
    path('registration/', registration, name='registration_done'),
    # 使用內建更改密碼 去呼叫模板
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='user/password_change.html'), name='password_change'),
    # 使用內建 views 去呼叫模板
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='user/password_change_done.html'), name='password_change_done'),
    # 使用內建logout views 去呼叫模板
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout')
]
