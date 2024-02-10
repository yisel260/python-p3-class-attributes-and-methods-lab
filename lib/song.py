class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    

    def __init__(self, name, artist, genre):
        self.increase_song_count()
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.update_genre_count(genre)
        self.update_artist_count(artist)


    @classmethod
    def increase_song_count(cls, increment=1):
        cls.count += increment
    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
           cls.artists.append(artist)
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def update_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def update_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
