from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', {
        'name': 'Nayra',
        'age': 30,
        'profission': 'Desenvolvedora',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', {
        'name': 'Nayra',
        'age': 30,
        'profission': 'Desenvolvedora',
    })
