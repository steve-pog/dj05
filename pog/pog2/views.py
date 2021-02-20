from django.shortcuts import render

# Create your views here.
def myhouse(request):
    info ={"key": "value of dictionary"}
    return render(request, 'anything.html', info)