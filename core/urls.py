from django.urls import path

from core.views import company_list,company_detail,company_vacancies

urlpatterns=[
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancies),

]