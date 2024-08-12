from django.shortcuts import render

import os
from django.http import JsonResponse
import yt_dlp
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import PlaylistForm

def download_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist_url = form.cleaned_data['url']
            output_dir = settings.MEDIA_ROOT
            
            # yt-dlp options
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best', #- for video and auddio,
                'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
                'noplaylist': False,
                'quiet': False,
                'writeinfojson': True,  # Write metadata to JSON files
            }
            
            # Download
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(playlist_url, download=True)
                
                # Fetch video info
                videos = []
                for entry in info_dict['entries']:
                    videos.append({
                        'title': entry['title'],
                        'url': entry['webpage_url'],
                        'thumbnail': entry['thumbnail'],
                    })
                
                return render(request, 'downloader/results.html', {'videos': videos})
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")
    else:
        form = PlaylistForm()
    return render(request, 'downloader/index.html', {'form': form})

def check_progress(request):
    progress = 50  # Replace with actual progress logic
    return JsonResponse({'progress': progress})