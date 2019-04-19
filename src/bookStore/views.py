from django.shortcuts import render


def index(request):
    context = {}
    context['message'] = 'Test Message'
    return render(request, 'index.html',context=context)
