from django.shortcuts import render


def home(request):
    context = {
        'name': 'Timur',
        'surname': 'Timerkaev',
        'age': 16,
        'interests': 'Programming, Reading'
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'origin': 'Djalil',
        'academic_performance': 'Python 1',
        'like_study': 'Yes'
    }
    return render(request, 'about.html', context)


def contacts(request):
    context = {
        'VK': 'https://vk.com/timurtimer1'
    }
    return render(request, 'contacts.html', context)


def chat(request):
    return render(request, 'chat.html')


def chat(request):
    return None
