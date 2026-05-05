from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view()),
    path('bookings/<int:pk>/', views.SingleBookingView.as_view()),
    path('registration/', views.RegisterView.as_view()),
    path('token/', obtain_auth_token),
]
