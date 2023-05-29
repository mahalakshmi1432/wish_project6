from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'maha'}
    return render(request,'wish.html',context=d)