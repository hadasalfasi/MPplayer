from song import Song
class Modern_Music (Song):
    def __init__(self, name, url, words):
        super(Modern_Music, self).__init__(name, url, words)
        self.rate = 75