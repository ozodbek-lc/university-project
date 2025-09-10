from django.shortcuts import render

def pages_index_view(request):
    return render(request,'index.html')
