from django.shortcuts import render
from .models import Recipe, Keywords


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

def testpage(request):
    return render(request,'testpage.html', {})


def all_recipes(request):
    recipe_list= Recipe.objects.all()
    return render(request, 'recipe_list.html',{'recipe_list':recipe_list})

def single_recipe(request,recipe_id):
    recipe=Recipe.objects.get(pk=recipe_id)
    return render(request, 'single_recipe.html', {'recipe': recipe})

def search_recipe(request):
    if request.method == "POST":
        searched = request.POST['tosearch']  # Receive the value of variable named 'keywords'
        results=Recipe.objects.filter(name__contains=searched)


        return render(request, 'search_recipe.html', {'tosearch': searched, 'results':results})  # Return the input variables to the server, and name it as searched.

    else:
        return render(request, 'search_recipe.html', {})


def Keywords_search(request,keywords_id):
    keywords=Keywords.objects.get(pk=keywords_id)
    return render(request, 'Keywords_search.html', {'keywords': Keywords})

def Ingredient_Search(request):
    if request.method == "POST":
        searched = request.POST['tosearch']  # Receive the value of variable named 'keywords'
        results=Recipe.objects.filter(name__contains=searched)


        return render(request, 'Ingredient_Search.html', {'tosearch': searched, 'results':results})  # Return the input variables to the server, and name it as searched.

    else:
        return render(request, 'Ingredient_Search.html', {})