# downloader/forms.py
from django import forms

class PlaylistForm(forms.Form):
    url = forms.URLField(label='YouTube Playlist URL', widget=forms.TextInput(attrs={'size': 80}))
