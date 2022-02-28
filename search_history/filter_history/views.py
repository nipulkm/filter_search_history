from django.shortcuts import render
from django.http import HttpResponse
from filter_history.controller import history_controller

def history(request):
    try:
        data = history_controller.get_history()
        return render(request, 'index.html', data)
    except Exception as exception:
        return HttpResponse(exception)