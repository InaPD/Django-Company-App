from django.urls import path
from .views import CompanyListView, CompanyDetailView, UserCompaniesView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('user-companies/', UserCompaniesView.as_view(), name='user-companies'),
]
