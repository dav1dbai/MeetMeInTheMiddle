from django.forms import ModelForm
from .models import Friend

class FriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "location"]