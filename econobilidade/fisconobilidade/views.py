from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "Hello to Fisconobilidade!"}
    return render(request,'fisconobilidade/index.html',context=my_dict)
