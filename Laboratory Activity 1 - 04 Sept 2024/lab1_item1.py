def get_music_info ():
    
    a = input ("Enter the year:")
    b = input ("Enter the genre: ")
    c = input ("Enter the album: ")
    d = input ("Enter the song title: ")
    e = input ("Enter the artist: ")

    print ("------------------")
    print ("SONG DETAILS")
    print ("------------------")
    
    print(f"year released: {a}")
    print(f"genre: {b}")
    print(f"album: {c}")
    print(f"title: {d}")
    print(f"artist: {e}")
    
get_music_info()
