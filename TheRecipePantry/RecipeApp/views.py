from django.shortcuts import render
from .models import Recipe

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
    return render(request,'testpage.html', {})


def all_recipes(request):
    recipe_list= Recipe.objects.all()
    return render(request, 'recipe_list.html',{'recipe_list':recipe_list})

def single_recipe(request,recipe_id):
    recipe=Recipe.objects.get(pk=recipe_id)
    return render(request, 'single_recipe.html', {'recipe': recipe})
def search_venues(request):
    if request.method == "POST":
        searched = request.POST['tosearch']  # Receive the value of variable named 'keywords'
       # recipes = Recipe.objects

        return render(request, 'search_venues.html', {'tosearch': searched})  # Return the input variables to the server, and name it as searched.
    else:
        return render(request, 'search_venues.html', {})
