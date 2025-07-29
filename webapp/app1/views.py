from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    names = ["JHUN", "JED", "STEVE"]
    # return HttpResponse("HELLO JHUN")
    return render(request, "dashboard.html", {'names': names})
