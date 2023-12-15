from django.shortcuts import render

posts=[
    {
        'title' : 'CS50SQL',
        'content' : 'Introduction to Databases with SQL',
        'author' : 'Carter Zenke',
        'date_posted' : 'December 14, 2023'
    },
    {
        'title' : 'CS50P',
        'content' : 'Introduction to Programming with Python',
        'author' : 'David Malan',
        'date_posted' : 'December 15, 2023'
    },
    {
        'title' : 'CS50Web',
        'content' : 'Introduction to Web Programming with Python and Javascript',
        'author' : 'Brian Yu',
        'date_posted' : 'December 16, 2023'
    }
]

# Create your views here.
def home(request):
    return render(request, "blog/home.html", {
        "posts": posts
    })

def about(request):
    return render(request, "blog/about.html", {
        'title': 'About'
    })