from django.shortcuts import render, reverse


def index(request):
    return render(request, 'index.html', {'sites': [1, 2, 3, 4, 5, 6, 7, 7, 8, 9,10, 11]})
