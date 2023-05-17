from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .forms import MessageForm
from .models import Service, Message


def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


# def service_list(request):
# services = Service.objects.all()
# return render(request, 'service_list.html', {'services': services})


def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    return render(request, 'booking.html', {'service': service})


def service_create(request):
    if request.method == 'POST':
        # Create a new service object with the form data
        form_data = request.POST
        service = Service(
            name=form_data['name'],
            description=form_data['description'],
            email=form_data['email'],
            date=form_data['date'],
        )
        service.save()
        print(" created")
        # Redirect to the service detail page
        return redirect('service_create')

    else:
        # Show the create service form
        return render(request, 'booking.html')


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('send_message')
        else:
            messages.error(request, 'Error sending the message. Please try again.')
    else:
        form = MessageForm()

    return render(request, 'contact.html')


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
