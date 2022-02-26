from django.shortcuts import render

posts = [
    {
        'name': 'Mansoud',
        'title': 'PM',
        'content': 'managing the team',
        'date_posted': 'today',
    },
    {
        'name': 'Bogdan',
        'title': 'Software Developer',
        'content': 'To write the code and develop the site.',
        'date_posted': 'yesterday',
    },
    {
        'name': 'Carlton',
        'title': 'Software Developer',
        'content': 'To write the code and develop the site with Bogdan',
        'date_posted': 'yesterday',
    },
    {
        'name': 'Matthew',
        'title': 'Security',
        'content': 'To test the site to potential threads and attack.',
        'date_posted': 'yesterday',
    },
    {
        'name': 'Abdullah',
        'title': 'DataBase',
        'content': 'to develop the databade for the site.',
        'date_posted': 'yesterday',
    },
    {
        'name': 'Dalvier',
        'title': 'Business',
        'content': 'To do the business part!!',
        'date_posted': 'yesterday',
    },
    {
        'name': 'Dilpreet',
        'title': 'Business',
        'content': 'You need to turn up for the meeting and all. I have no idea what you up to!',
        'date_posted': 'yesterday',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'frackHub/home.html', context)


def about(request):
    return render(request, 'frackHub/about.html')
