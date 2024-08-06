import pygame
class Song:
    def __init__(self, name='unknown',url='unknown', words=''):

        self.name = name
        self.url = url
        self.words = open(file=r"C:\Users\1\Desktop\הדס\לימודים\שנה ב\PHYTON\final proj\New folder\{}.txt".format(self.name),mode='ta',encoding='utf-8')
        self.words.write(words)
        self.words.close()

    def print_words(self):
        """print the words of song"""
        self.words = open(file=r"C:\Users\1\Desktop\הדס\לימודים\שנה ב\PHYTON\final proj\New folder\{}.txt".format(self.name), mode='tr',
                          encoding='utf-8')
        self.words.seek(0)
        print(self.words.read())
        self.words.close()
    def singSong(self):
        """turn on a song"""
        try:
            pygame.init()
            pygame.mixer.music.load(self.url)
            pygame.mixer.music.play()
            stop = input('to stop press x')
            if stop == 'x':
                pygame.mixer.music.stop()
            while pygame.mixer.music.get_busy():
                continue
            pygame.quit()
        except:
            print('url not valid!')

