from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Baby, Post
from .forms import BabyForm, PostForm


def check_baby_owner(request, baby):
    # Make sure the baby belongs to the current user.
    if baby.owner != request.user:
        raise Http404


def index(request):
    """Home page for baby_log"""
    return render(request, "baby_logs/index.html")


@login_required
def babies(request):
    """babies page for baby_log"""
    babies = Baby.objects.filter(owner=request.user).order_by("date_added")
    context = {"babies": babies}
    return render(request, "baby_logs/babies.html", context)


@login_required
def baby(request, baby_id):
    """Single baby page"""
    baby = Baby.objects.get(id=baby_id)

    check_baby_owner(request, baby)

    posts = baby.post_set.order_by("-date_of_event")
    context = {"baby": baby, "posts": posts}
    return render(request, "baby_logs/baby.html", context)


@login_required
def new_baby(request):
    """Add new baby"""
    if request.method != "POST":
        # No data submitted, create a blank form
        form = BabyForm()
    else:
        # POST data submitted, process data
        form = BabyForm(data=request.POST)
        if form.is_valid():
            new_baby = form.save(commit=False)
            new_baby.owner = request.user
            new_baby.save()
            return redirect("baby_logs:babies")

    context = {"form": form}
    return render(request, "baby_logs/new_baby.html", context)


@login_required
def delete_baby(request, baby_id):
    """Delete a baby"""
    baby = Baby.objects.get(id=baby_id)

    check_baby_owner(request, baby)
    baby.delete()

    return redirect("baby_logs:babies")


@login_required
def new_post(request, baby_id):
    """Add new baby"""
    baby = Baby.objects.get(id=baby_id)

    # Make sure the baby belongs to the current user.
    check_baby_owner(request, baby)

    if request.method != "POST":
        # No data submitted, create a blank form
        form = PostForm()
    else:
        # POST data submitted, process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.baby = baby
            new_post.save()
            return redirect("baby_logs:baby", baby_id=baby_id)

    context = {"form": form, "baby": baby}
    return render(request, "baby_logs/new_post.html", context)


@login_required
def edit_post(request, post_id):
    """Edit a post"""
    post = Post.objects.get(id=post_id)
    print(post)
    baby = post.baby

    # Make sure the baby belongs to the current user.
    check_baby_owner(request, baby)

    if request.method != "POST":
        # No data submitted, create a blank form
        form = PostForm(instance=post)
    else:
        # POST data submitted, process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("baby_logs:baby", baby_id=baby.id)

    context = {"post": post, "form": form, "baby": baby}
    return render(request, "baby_logs/edit_post.html", context)


@login_required
def delete_post(request, post_id):
    """Delete a post"""
    post = Post.objects.get(id=post_id)
    baby = post.baby

    # Make sure the baby belongs to the current user.
    check_baby_owner(request, baby)

    post.delete()

    return redirect("baby_logs:baby", baby_id=baby.id)
