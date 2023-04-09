from django.shortcuts import render

from django.http import HttpResponse

def main_page(request):
    
    return HttpResponse('<html> <h1> main </h1></html>')
    
def root_page(request):
    
    return render(request, 'root_page.html')