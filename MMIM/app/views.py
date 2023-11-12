from django.shortcuts import render, get_object_or_404
from .models import Friend
from .forms import FriendForm

# Create your views here.

users = {}

def index(request):
    if request.method == "POST":
        print(request.POST.get("name"))
        FriendInstance = get_object_or_404(Friend, name=request.POST.get("name"))
        context = FriendInstance.getRec()
        return render(request, "index.html", {"context": context})
    context = ""
    return render(request, "index.html", {"context": context})

def friends(request):
    if request.method == "POST":
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
    print(Friend.objects.filter().values())
    form = FriendForm()
    return render(request, "friends.html", {"form": form, "friends": Friend.objects.filter().values()})