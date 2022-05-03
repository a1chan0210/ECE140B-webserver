from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def KVP(request):
    return render(request, 'KVP.html')

def LawsofUI(request):
    return render(request, 'LawsofUI.html')