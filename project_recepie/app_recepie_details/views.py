from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe


def home(request):
    # return HttpResponse("Hello, Django!")
    
    recipe_list = Recipe.objects.all()   
    output = ", ".join(recp.recipe_name for recp in recipe_list)
    print(output)
    
    context = { # dictionary
        "recipe_list": recipe_list,
    }
    return render(request, "app_recepie_details/index.html", context)


def detail(request, recp_id):
    return HttpResponse(f"You're looking at recipie {recp_id}")