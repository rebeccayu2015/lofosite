from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.MyLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout, name='logout'),
    # path('reset-password/', views.MyPasswordResetView.as_view(), name='reset_password'),
    # path('reset-password/sent/', views.MyPasswordResetDoneView.as_view(), name='reset_password_sent'),
    # path('reset-password/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    # path('reset-password/done/', views.MyPasswordResetCompleteView.as_view(), name='reset_password_complete'),
    # path('change-password/', views.MyPasswordChangeView.as_view(), name='change_password'),
    # path('change-password/done/', views.MyPasswordChangeCompleteView.as_view(), name='change_password_complete'),
    path('profile/', views.profile, name='profile')
]
