from genericpath import exists
import lyricsgenius as lg
import os
#if(exists("/Users/User/Desktop/auto_.txt")):
file = open('C:/Users/User/Desktop/auto_.txt', 'w')
genius = lg.Genius('ZmGunvTbssfWj6HToiES_LIgMEIlv9HI1aliLbo9iUpvsyvc5DsP4em1lgiQj-uB',
skip_non_songs=True, excluded_terms=["(Remix) , (Live)"],
remove_section_headers=True )

def get_lyrics(arr,k):
    print(arr)
    c = 0
    for name in arr:
        print(name)
        #try:
         #   print(name)
        songs = (genius.search_artist(name,max_songs=k,sort='popularity')).songs
        s = [song.lyrics for song in songs]
        file.write("\n\n  <|endoftext|>  \n\n".join(s))
        c += 1
        print (f"Songs grabbed: {len(s)}")
        #except:
        print(f"some exeption at {name}: {c}")


band_names = ['linkin park', 'ac/dc']
artists = ['Logic', 'Rihanna', 'Frank Sinatra']

get_lyrics(band_names,20)
print("Done")