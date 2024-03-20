from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def ourgoal(request):
    return render(request, 'ourgoal.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def questionnaire(request):
    return render(request, 'questionnaire.html')

def recipes(request):
    return render(request, 'recipes.html')

def testpage(request):
    return render(request,'testpage.html',{})

def search_venues(request):
    if request.method=="POST":
        searched=request.POST['searched']

        return render(request, 'search_venues.html',{'searched':searched})
    else:
        return render(request, 'search_venues.html',{})