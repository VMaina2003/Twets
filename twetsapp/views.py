from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Twet
from .forms import TwetForm
from django.contrib.auth import logout
from django.shortcuts import redirect




@login_required
def feed_view(request):
    twets = Twet.objects.all()
    return render(request, 'twets/feed.html', {'twets': twets})

@login_required
def create_twet(request):
    if request.method == 'POST':
        form = TwetForm(request.POST, request.FILES)
        if form.is_valid():
            twet = form.save(commit=False)
            twet.user = request.user
            twet.save()
            return redirect('feed')
    else:
        form = TwetForm()
    return render(request, 'twets/create_twet.html', {'form': form})

@login_required
def twet_detail(request, id):
    twet = get_object_or_404(Twet, id=id)
    return render(request, 'twets/twet_detail.html', {'twet': twet})


@login_required
def edit_twet(request, id):
    twet = get_object_or_404(Twet, id=id, user=request.user)  # only owner can edit
    if request.method == 'POST':
        form = TwetForm(request.POST, request.FILES, instance=twet)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = TwetForm(instance=twet)
    return render(request, 'twets/edit_twet.html', {'form': form, 'twet': twet})


@login_required
def delete_twet(request, id):
    twet = get_object_or_404(Twet, id=id, user=request.user)  # only owner can delete
    if request.method == 'POST':
        twet.delete()
        return redirect('feed')
    return render(request, 'twets/delete_twet.html', {'twet': twet})