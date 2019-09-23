from django.shortcuts import render


def dashboard(request):
    return render(request, 'negotiations/dashboard.html')


def keywords(request):
    return render(request, 'negotiations/keywords.html')


def subject(request):
    return render(request, 'negotiations/subject.html')


def common_factors(request):
    return render(request, 'negotiations/commonfactors.html')
