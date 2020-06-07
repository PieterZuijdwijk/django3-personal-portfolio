from django.shortcuts import render
from .models import About, Contact, Education, Interests, Internship, Project, Work

def home(request):
    projects = Project.objects.all()
    abouts = About.objects.all()
    works = Work.objects.all()
    internships = Internship.objects.all()
    education = Education.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects, 'abouts':abouts, 'works':works, 'internships':internships, 'education':education})
