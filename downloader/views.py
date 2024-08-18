import yt_dlp
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PlaylistForm


def format_filesize(size_in_bytes):
    # Convert size in bytes to a human-readable format
    if size_in_bytes is None:
        return "Unknown Size"
    size_in_bytes = float(size_in_bytes)
    KB = 1024
    MB = KB * 1024
    GB = MB * 1024

    if size_in_bytes < KB:
        return f"{size_in_bytes:.2f} Bytes"
    elif size_in_bytes < MB:
        return f"{size_in_bytes / KB:.2f} KB"
    elif size_in_bytes < GB:
        return f"{size_in_bytes / MB:.2f} MB"
    else:
        return f"{size_in_bytes / GB:.2f} GB"


def filter_direct_links(formats):
    # Filter out formats to include only those with a definite size and in mp4 format
    return [
        {
            'url': fmt.get('url'),
            'format_id': fmt.get('format_id'),
            'height': fmt.get('height'),
            'filesize': format_filesize(fmt.get('filesize')),
            'ext': fmt.get('ext')
        }
        for fmt in formats
        if fmt.get('filesize') is not None and fmt.get('ext') == 'mp4'
    ]


def get_download_links(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist_url = form.cleaned_data['url']
            
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'noplaylist': False,
                'quiet': True,
                'skip_download': True,
            }
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(playlist_url, download=False)
                
                videos = []
                if 'entries' in info_dict:
                    entries = info_dict['entries']
                else:
                    entries = [info_dict]
                
                for entry in entries:
                    formats = entry.get('formats', [])
                    
                    filtered_formats = filter_direct_links(formats)
                    
                    if filtered_formats:
                        highest_quality = max(filtered_formats, key=lambda f: f.get('height', 0))
                        highest_quality_link = highest_quality.get('url')
                        highest_quality_resolution = f"{highest_quality.get('height')}p"
                    else:
                        highest_quality_link = None
                        highest_quality_resolution = "N/A"
                    
                    video_info = {
                        'title': entry.get('title'),
                        'highest_quality_link': highest_quality_link,
                        'highest_quality_resolution': highest_quality_resolution,
                        'formats': filtered_formats,
                        'thumbnail': entry.get('thumbnail'),
                    }
                    videos.append(video_info)
                
                return render(request, 'downloader/results.html', {'videos': videos})
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")
    else:
        form = PlaylistForm()
    return render(request, 'downloader/index.html', {'form': form})
