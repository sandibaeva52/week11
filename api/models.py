from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')
def short(self):
    return '{}: {}'.format(self.id, self.name,self.description,self.city,self.address)
def full(self):
    return{
            'id': self.id,
            'name': self.name,
            'description':self.description,
            'city': self.city,
             'address':self.address
    }
class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='vacancies')

    def short(self):
        return '{}: {}'.format(self.id, self.name, self.description, self.salary, self.company)

    def full(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company
        }