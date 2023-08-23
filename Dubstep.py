'''
Input
The input consists of a single non-empty string, consisting only of uppercase English letters,
the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix.
Separate the words with a space.

Examples
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND

'''

#Nuaiman's Solution (contains IndexError)
def song_decoder(song):
    if song[:3] == 'WUB':
        song = song.lstrip("WUB")
    if song[len(song)-3:] == "WUB":
        song = song.rstrip("WUB")
    song = song.replace("WUB", "#")    
    SongArray = list(song)
    
    FinalSong = " " 
    for n in range(len(SongArray)-1):
        if SongArray[n] != "#":
            if SongArray[n+1] == "#":
                FinalSong = FinalSong + SongArray[n] + " "
            else:
                FinalSong = FinalSong +SongArray[n]
               
    FinalSong = FinalSong.lstrip() + SongArray[len(SongArray)-1]            
    
                   
    return FinalSong

#Solution 1
def song_decoder(song):
    index = 0
    remix = ""
    remix = song.replace("WUB", ' ')
    remixarr = remix.split()
    return ' '.join(remixarr)

#Solution 2
def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())



