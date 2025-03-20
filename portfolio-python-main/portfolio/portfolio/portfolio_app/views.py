from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
def  index(request):
    return render(request,'index.html')
def  resume(request):
    return render(request,'resume.html')
# Create your views here.
def  contact(request):
    return render(request,'contact.html')
def Certificate_view(request):
    certificates = Certificate.objects.all()  # Fetch all certificates from the database
    return render(request, 'certificate.html', {'certificates': certificates})
def certificate_detail_view(request, title):
    certificate = get_object_or_404(Certificate, title=title)  # Fetch certificate by title
    return render(request, 'certificate_detail.html', {'certificate': certificate})