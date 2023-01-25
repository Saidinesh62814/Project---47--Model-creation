from django.shortcuts import render

# Create your views here.
def Child(request):
    return render(request,'Child.html')

def Parent(request):
    return render(request,'Parent.html')

