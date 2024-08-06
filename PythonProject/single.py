from song import Song
from modernMusic import Modern_Music
from music import Class_Music
class Singer:
    def __init__(self, name='unknown'):
        self.name = name
        self.songs_arr =[]

    def add_song(self, song):
        """add song for songs_arr to a specific singer"""
        if song in self.songs_arr:
            print('The song exist')
        else:
            self.songs_arr.append(song)
            print('The song was successfully added')

    def print_songs_name(self):
        """Printing the song list of the singer on whom the function is activated"""
        print(f"The songs of {self.name} are:")
        def generator(arr):
            for i in arr:
                yield i
        for i in generator(self.songs_arr):
            print(i.name)
        """print by generator"""