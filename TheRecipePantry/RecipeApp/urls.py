from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ourgoal/', views.ourgoal, name='ourgoal'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('testpage/', views.testpage, name='testpage'),
    path('search_recipe/', views.search_recipe, name='search-recipe'),
    path('recipe_list', views.all_recipes, name='recipe-list'),
    path('single_recipe/<recipe_id>', views.single_recipe, name='single-recipe'),
    path('Keywords_search/<keywords_id>', views.Keywords_search, name='Keywords_search'),
    path('Ingredient_Search/', views.Ingredient_Search, name='Ingredient_Search'),
]