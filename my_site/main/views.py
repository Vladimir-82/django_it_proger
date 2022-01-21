from django.shortcuts import render
# Create your views here.

content = {
    'key1': 1,
    'values': ['Some', 'Hello', '123']
}



def index(request):
    return render(request, 'main/index.html', content)

def about(request):
    return render(request, 'main/about.html')

