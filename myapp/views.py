from rest_framework import generics, permissions,serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer
from rest_framework.authentication import TokenAuthentication
from django.http.response import JsonResponse
from django.core.mail import send_mail


class CompanyListViewPagination(PageNumberPagination):
    page_size = 3 
    page_size_query_param = 'page_size'
    max_page_size = 100


class CompanyListView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    pagination_class = CompanyListViewPagination

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user).order_by('id') 
    
    def list(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = [{"company_name": item["company_name"], "description": item["description"], "number_of_employees": item["number_of_employees"]} for item in serializer.data]
            return self.get_paginated_response(data)

        # Serialize only specific fields
        # serializer = self.get_serializer(queryset, many=True)
        # data = [{"company_name": item["company_name"], "description": item["description"], "number_of_employees": item["number_of_employees"]} for item in serializer.data]

        # return Response(data)

    def perform_create(self, serializer):
        user = self.request.user
        # Check if the user has already created 5 companies
        if Company.objects.filter(owner=user).count() >= 5:
            raise serializers.ValidationError("You have reached the maximum limit of 5 companies.")

        instance =serializer.save(owner=self.request.user)
        # Add email sending logic here
        if user.email:
            send_email(user.email, instance.company_name)

class CompanyDetailView(generics.RetrieveUpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def update(self, request, *args, **kwargs):
        # Retrieve the company instance
        instance = self.get_object()

        # Check if the user is the owner of the company
        if request.user != instance.owner:
            return Response({"detail": "You don't have permission to update this company."}, status=403)

        # Update only the 'number_of_employees' field
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class UserCompaniesView(generics.ListAPIView):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)
    
def send_email(email, company_name):
        subject = 'Company Created'
        message = f'Thank you for creating a new company: {company_name}.'
        from_email = 'your_email@example.com'  # Update with your email address or use a dedicated email account
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)
