from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def check_topic_owner(request, topic):
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404


def index(request):
    """Home page for baby_log"""
    return render(request, "baby_logs/index.html")


@login_required
def topics(request):
    """Topics page for baby_log"""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "baby_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    """Single topic page"""
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "baby_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != "POST":
        # No data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted, process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("baby_logs:topics")

    context = {"form": form}
    return render(request, "baby_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add new topic"""
    topic = Topic.objects.get(id=topic_id)

    # Make sure the topic belongs to the current user.
    check_topic_owner(request, topic)

    if request.method != "POST":
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("baby_logs:topic", topic_id=topic_id)

    context = {"form": form, "topic": topic}
    return render(request, "baby_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit a entry"""
    entry = Entry.objects.get(id=entry_id)
    print(entry)
    topic = entry.topic

    # Make sure the topic belongs to the current user.
    check_topic_owner(request, topic)

    if request.method != "POST":
        # No data submitted, create a blank form
        form = EntryForm(instance=entry)
    else:
        # POST data submitted, process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("baby_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "form": form, "topic": topic}
    return render(request, "baby_logs/edit_entry.html", context)
