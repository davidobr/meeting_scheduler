from django.shortcuts import render


def homepage(request):
    return render(request, 'website/homepage.html')


def meeting(request):
    return render(request, 'website/meetings.html')
