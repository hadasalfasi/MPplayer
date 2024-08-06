from song import Song
class Class_Music (Song):
    def __init__(self, name,url, words):
        super(Class_Music, self).__init__(name,url, words)
        self.rate = 150