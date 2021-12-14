from django.shortcuts import render
from .models import Donor, Post

def home(request):
    return render(request, 'organ/homepage.html')


def read(request):
    return render(request, 'organ/read.html')


def family(request):
    oDonors = Donor.objects.filter(type__name='organ donor').order_by('-date_created')
    bDonors = Donor.objects.filter(type__name='blood donor').order_by('-date_created')
    volunteer = Donor.objects.filter(type__name='volunteer').count()
    recipient = Donor.objects.filter(type__name='organ recipient').count()
    organ = oDonors.count()
    blood = bDonors.count() 

    return render(request, 'organ/family.html', {'oDonors':oDonors, 'bDonors':bDonors,
    'volunteer':volunteer, 'recipient':recipient, 'organ':organ, 'blood':blood})


def stories(request):
    oStory = Post.objects.order_by('-created_date')

    
    return render(request, 'organ/stories.html', {'oStory':oStory})


def donor_story(request, pk):
    
    return render(request, 'organ/donor_story.html')


def terms(request):
    return render(request, 'organ/terms.html')


def about(request):
    return render(request, 'organ/about.html')

