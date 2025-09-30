from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Twet

@login_required
def feed_view(request):
    twets = Twet.objects.all().order_by('-created_at')
    return render(request, 'twets/feed.html', {'twets': twets})

@login_required
def create_twet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Twet.objects.create(user=request.user, content=content)
            return redirect('feed')
    return render(request, 'twets/create_twet.html')

@login_required
def twet_detail(request, id):
    twet = get_object_or_404(Twet, id=id)
    return render(request, 'twets/twet_detail.html', {'twet': twet})
