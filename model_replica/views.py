from django.http import HttpResponse
from russian_names import RussianNames

from .models import Worker


def create_workers(request):
    fio = RussianNames(count=10).get_batch()
    response = 'Ряды наших сотрудников пополнили:'
    for i in range(10):
        worker = Worker(fio=fio[i])
        worker.save()
        response += f' {worker}'

    return HttpResponse()


def main_db(request):
    workers = Worker.objects.all()
    response = 'Данные о сотрудниках из основной базы данных:'
    for worker in workers:
        response += f' {worker}'
    return HttpResponse(response)


def replica_db(request):
    workers = Worker.objects.using('replica_1').all()
    response = 'Данные о сотрудниках из реплики базы данных:'
    for worker in workers:
        response += f' {worker}'
    return HttpResponse(response)

