from django.shortcuts import render


def trans_table(request):
    return render(request, 'summaries/summary.html')