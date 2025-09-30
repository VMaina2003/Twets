from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet

@login_required
def feed(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Tweet.objects.create(user=request.user, content=content)
            return redirect("feed")
    return render(request, "twets/feed.html", {"tweets": tweets})
