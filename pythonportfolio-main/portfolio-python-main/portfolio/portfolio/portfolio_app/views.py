from django.http import FileResponse, Http404
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from django.contrib import messages

def  index(request):
    return render(request,'index.html')

# Create your views here.
def  contact(request):
    return render(request,'contact.html')
def Certificate_view(request):
    certificates = Certificate.objects.all()  # Fetch all certificates from the database
    return render(request, 'certificate.html', {'certificates': certificates})
def certificate_detail_view(request, title):
    certificate = get_object_or_404(Certificate, title=title)  # Fetch certificate by title
    return render(request, 'certificate_detail.html', {'certificate': certificate})
from django.shortcuts import render
from .models import Resume

def resume_view(request):
    resume = Resume.objects.first()  # Fetch only the first resume
    return render(request, 'resume.html', {'resume': resume})
def download_resume(request):
    resume = Resume.objects.last()  # Fetch the first resume
    if resume and resume.resume_file:
        return FileResponse(resume.resume_file.open(), as_attachment=True, filename=resume.resume_file.name)
    else:
        raise Http404("Resume not found")
def delete_certificate(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    certificate.delete()
    return redirect('certificate')
def upload_certificate(request):
    if request.method == 'POST':
        title = request.POST['title']
        issuer = request.POST['issuer']
        issue_date = request.POST['issue_date']
        certificate_file = request.FILES['certificate_file']

        Certificate.objects.create(
            title=title,
            issuer=issuer,
            issue_date=issue_date,
            certificate_file=certificate_file
        )
        return redirect('certificate')  # Redirect to certificate list

    return render(request, 'certificate.html')


class ContactMessage:
    pass


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:  # Ensure all fields are filled
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")  # ✅ Success Message
            return redirect('contact')  # Redirect back to the contact page

        else:
            messages.error(request, "All fields are required!")  # If any field is empty

    return render(request, 'contact.html')
