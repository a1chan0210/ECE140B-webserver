from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def KVP(request):
    return render(request, 'KVP.html')

def LawsofUI(request):
    return render(request, 'LawsofUI.html')

def ProductIA(request):
    return render(request, 'productIA.html')

def FeatureBenefit(request):
    return render(request, 'featurebenefit.html')

def Interaction(request):
    return render(request, 'interaction.html')

def Revenue(request):
    return render(request, 'revenue.html')

def Pivot(request):
    return render(request, 'pivot.html')