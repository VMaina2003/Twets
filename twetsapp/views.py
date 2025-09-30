from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Twet, Like, Comment
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
def like_twet(request, id):
    twet = get_object_or_404(Twet, id=id)
    like, created = Like.objects.get_or_create(user=request.user, twet=twet)
    if not created:  # already liked → unlike
        like.delete()
    return redirect('feed')


@login_required
def add_comment(request, id):
    twet = get_object_or_404(Twet, id=id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content.strip():
            Comment.objects.create(user=request.user, twet=twet, content=content)
    return redirect('feed')


@login_required
def twet_detail(request, id):
    twet = get_object_or_404(Twet, id=id)
    comments = twet.comments.all().order_by("-created_at")

    if request.method == "POST":
        content = request.POST.get("content")
        if content.strip():
            Comment.objects.create(user=request.user, twet=twet, content=content)
            return redirect("twet_detail", id=twet.id)  # refresh same page

    return render(
        request,
        "twets/twet_detail.html",
        {"twet": twet, "comments": comments},
    )
    
    
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

@login_required
def feed_view(request):
    twets = Twet.objects.all().order_by("-created_at")
    return render(request, 'twets/feed.html', {"twets": twets})


@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    # only the comment owner can delete
    if comment.user == request.user:
        twet_id = comment.twet.id
        comment.delete()
        return redirect("twet_detail", id=twet_id)
    else:
        return redirect("twet_detail", id=comment.twet.id)