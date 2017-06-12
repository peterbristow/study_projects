from django.shortcuts import get_object_or_404, render

from .models import Song, Performer

"""
* Views:
  * list view, all of the songs
  * detail view, a particular song
    * tell who's performing it
  * performer view, a particular performer
    * list all of their songs
"""

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'songs/song_detail.html', {'song': song})
  
def performer_detail(request, pk):
    performer = get_object_or_404(Performer, pk=pk)
    performer.song_set.all()
    return render(request, 'songs/performer_detail.html', {'performer': performer})
 