from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return render(request, "resumebuilder/landing_page.html")

def index(request):
    return HttpResponse("Hello, world. You're at the resume builder index.")

def create(request):
    return HttpResponse("Resume created")

def read(request, resume_id):
    response = "Retrieved resume with id %s"
    return HttpResponse(response % resume_id)

def update(request):
    return HttpResponse("Resume updated")

def delete(request):
    return HttpResponse("Resume deleted")