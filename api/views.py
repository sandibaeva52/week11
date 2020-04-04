from django.http import JsonResponse
from api.models import Company,Vacancy
companies = [{
    'id': i,
    'name': f'company{i}',
    'description': f'company{i}',
    'city': f'company{i}',
    'address': f'company{i}'
} for i in range(1, 5)
]
vacancies = [{
    'id': j,
    'name': f'vacancy{j}',
    'description': f'vacancy{j}',
    'salary':  j*1000,
    'company': f'vacancy{j}'
} for j in range(1,5)]


def company_list(request):
    companies = Company.objects.all()
    companies_json = [c.full() for c in companies]
    return JsonResponse(companies_json, safe=False)


def company_detail(request, company_id):
    if request.method == "GET":
        try:
            companies = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse(companies.full())
    elif request.method == 'POST':
        # Must create new Product from request body
        pass

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.full() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request):
    if request.method == "GET":
        try:
            vacancies = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse(vacancies.full())
    elif request.method == 'POST':
        # Must create new Product from request body
            pass


def company_vacancies(request, company_id):
    if request.method == "GET":
        try:
            companies = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        vacancies = companies.vacancies.all()
        vacancies_json = [v.full() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        # Must create new Product from request body
        pass

def vacancy_topten(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        vacancies_json = [v.short() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        # Must create new Product from request body
        pass
