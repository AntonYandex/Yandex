from django.shortcuts import render


def about(request):
    """Display about page."""
    return render(request, 'pages/about.html')


def rules(request):
    """Display rules page."""
    return render(request, 'pages/rules.html')
