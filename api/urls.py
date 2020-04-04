from django.urls import path

from api.views import vacancy_list,vacancy_detail,vacancy_topten

urlpatterns = [
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancy_topten),

]