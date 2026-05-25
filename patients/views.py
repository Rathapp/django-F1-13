from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from django.db.models import Q

# Create your views here.
def home(request):
    
    return render(request,'patients/home.html')


def about(request):
    patient = Patient.objects.filter(Q(dob__gt='2000-01-01') | Q(dob__lt='2003-01-01'))

    return render(request,'patients/about.html',{'patient':patient})

def register(request):
    people = [
    {
        "id": 1,
        "name": "John Smith",
        "age": 28,
        "job": "Software Engineer",
        "image": "https://randomuser.me/api/portraits/men/1.jpg"
    },
    {
        "id": 2,
        "name": "Emma Johnson",
        "age": 25,
        "job": "Graphic Designer",
        "image": "https://randomuser.me/api/portraits/women/2.jpg"
    },
    {
        "id": 3,
        "name": "Michael Brown",
        "age": 32,
        "job": "Doctor",
        "image": "https://randomuser.me/api/portraits/men/3.jpg"
    },
    {
        "id": 4,
        "name": "Sophia Davis",
        "age": 27,
        "job": "Teacher",
        "image": "https://randomuser.me/api/portraits/women/4.jpg"
    },
    {
        "id": 5,
        "name": "Daniel Wilson",
        "age": 35,
        "job": "Chef",
        "image": "https://randomuser.me/api/portraits/men/5.jpg"
    },
    {
        "id": 6,
        "name": "Olivia Taylor",
        "age": 24,
        "job": "Photographer",
        "image": "https://randomuser.me/api/portraits/women/6.jpg"
    },
    {
        "id": 7,
        "name": "James Anderson",
        "age": 30,
        "job": "Architect",
        "image": "https://randomuser.me/api/portraits/men/7.jpg"
    },
    {
        "id": 8,
        "name": "Isabella Thomas",
        "age": 29,
        "job": "Nurse",
        "image": "https://randomuser.me/api/portraits/women/8.jpg"
    },
    {
        "id": 9,
        "name": "William Martinez",
        "age": 31,
        "job": "Police Officer",
        "image": "https://randomuser.me/api/portraits/men/9.jpg"
    },
    {
        "id": 10,
        "name": "Mia Garcia",
        "age": 26,
        "job": "Data Analyst",
        "image": "https://randomuser.me/api/portraits/women/10.jpg"
    }
]


    
    return render(request,'patients/register.html',{"peoples":people})

