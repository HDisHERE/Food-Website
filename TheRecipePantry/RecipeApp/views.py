from django.shortcuts import render
from django.db.models import Q
from .models import Recipe, Keywords
from .filters import RecipeFilter


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

    category=request.GET.get('category')
    if request.method == "POST":
        searched = request.POST['tosearch']  # Receive the value of variable named 'keywords'
        all_recipe=Recipe.objects.all()
        #results_name=Recipe.objects.filter(Q(name__contains=searched)|Q(keywords__contains=searched))
        results=Recipe.objects.filter(Q(keywords__contains=searched)|Q(name__contains=searched)).distinct()
        myFilter = RecipeFilter(request.GET,queryset=results)
        results=myFilter.qs
        context={
                'tosearch': searched,
                'results': results,
                'all_recipe': all_recipe,
                'myFilter' : myFilter
        }



        return render(request, 'search_recipe.html', context)  # Return the input variables to the server, and name it as searched.

    else:
        return render(request, 'search_recipe.html', {})


def Keywords_search(request,keywords_id):
    keywords=Keywords.objects.get(pk=keywords_id)
    return render(request, 'Keywords_search.html', {'keywords': Keywords})

def Ingredient_Search(request):
    if request.method == "POST":
        searched = request.POST['tosearch']  # Receive the value of variable named 'keywords'
        results=Recipe.objects.filter(keywords__contains=searched)


        return render(request, 'Ingredient_Search.html', {'tosearch': searched, 'results':results})  # Return the input variables to the server, and name it as searched.

    else:
        return render(request, 'Ingredient_Search.html', {})