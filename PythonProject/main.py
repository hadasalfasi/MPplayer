from song import Song
from modernMusic import Modern_Music
from single import Singer
s=Song('HeapOfMiss',r'C:\Users\1\Downloads\יותר גדול מזה = יפוש ברכהן 🎵.mp3')
s.print_words()
a=Modern_Music('Tfila',r'C:\Users\1\Downloads\יותר גדול מזה = יפוש ברכהן 🎵.mp3')
sin=Singer("hadas")
sin.add_song(s)
sin.add_song(a)
sin2=Singer("efrat")
sin2.add_song(a)
singerarr=[sin,sin2]
favoritesongs1=[]
favoritesongs2=[]
favoritesongs3=[]
arrSongs=[s,a]
arrfavorite={'1':favoritesongs1,'2':favoritesongs2,'3':favoritesongs3}
def survey(nameSong,age):
    a=lambda age:int(int(age)/10)
    if a==1:
        arrfavorite['1'].append(nameSong)
        print('thank you for your participent in the survey!')
    elif a==2:
        arrfavorite['2'].append(nameSong)
        print('thank you for your participent in the survey!')
    else:
        arrfavorite['3'].append(nameSong)
        print('thank you for your participent in the survey!')

print('welcome to your player!')
x=int(input('For the playlist press 1,\n to hear a particular song press 2,\n to add a song press 3,\n  to read the lyrics press 4,\n to join the survey of favorite songs press 5,\n to list songs by singer press 6\n to exit press "-1" '))
while(x!=-1):
    if x==1 :
        for i in arrSongs:
            i.singSong()
    elif x==2:
        f = 0
        str = input('Which singer would you like to hear?')
        f1 = 0
        for i in singerarr:
            if f1==1:
                break
            if i.name == str:
                f = 1
                i.print_songs_name()
                str2 = input(r'which song do you want to hear?')

                for j in i.songs_arr:
                    if j.name == str2:
                        f1=1
                        j.singSong()
                        break
                if f1==0:
                    print("The song not found")
        if f==0:
            print('This singer not found')
    elif x == 3:
        help = 0
        n = input("what the song name?")
        u = input('what is the url of this song?')
        w = input('what is the words of this song?')
        z = input('whitch single sung this song?')
        for i in singerarr:
            if z == i.name:
                help = 1
                newsong = Song(n, u, w)
                i.add_song(newsong)
                break
        if help == 0:
            newzamar = Singer(z)
            singerarr.append(newzamar)
            newsong = Song(n, u, w)
            newzamar.add_song(newsong)
        arrSongs.append(newsong)
    elif(x==4):
        f=0
        txt=input('which song would you want to read?')
        for i in arrSongs:
            if i.name==txt:
                i.print_words()
                f=1
        if f==0:
            print('the song not found')
    elif x==5:
        name=input('enter songName you like?')
        age=input('enter your age')
        survey(name,age)
    elif(x==6):
        name=input('who is the singer?')
        for i in singerarr:
            if i.name==name:
                i.print_songs_name()
    else:print('eror!')
    x=int(input('For the playlist press 1,\n to hear a particular song press 2,\n to add a song press 3,\n  to read the lyrics press 4,\n to join the survey of favorite songs press 5,\n to list songs by singer press 6\n to exit press "-1" '))

