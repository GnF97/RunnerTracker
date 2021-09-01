from django.urls import path
from . import views, viewsA
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("shoez/<int:pk_shoe>/", views.shoez, name="shoez"),
    path("shoez/modify/<int:pk_run>/", views.modify_run, name="modify_run"),
    path("shoez/add_run/<int:pk_shoe>/", views.add_run, name="add_run"),
    path("shoez/retire_shoe/<int:pk_shoe>/", views.retire_shoe, name="retire_shoe"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_run/", views.create_run, name="create_run"),
    
    path("register/",viewsA.registerPage, name="register"),
    path("login/",viewsA.loginPage, name="login"),
    path("logout/",viewsA.logoutUser, name="logout"),
    path("user/", views.userPage, name="userpage"),
    path("clothset_info/", views.clothsetInfo, name="clothset_info"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="Accounts/password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="Accounts/password_reset_sent.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="Accounts/password_reset_form.html"), 
     name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="Accounts/password_reset_done.html"), 
        name="password_reset_complete"),
    ]
