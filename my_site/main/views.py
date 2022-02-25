from django.shortcuts import render

content = {
    'key1': 1,
    'values': ['Some', 'Hello', '123']
}



def index(request):
    return render(request, 'main/index.html', content)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

