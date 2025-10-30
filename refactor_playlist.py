
class Playlist():

    def __init__(self, name):
        self.name = name
        self.playlist = []
        self.__value__ = 12

    def show_playlist(self):
        """ """
        for i, song in enumerate(self.playlist, start=1):
            print(f"{i} {song}")

    def add_song(self, title: str):
        self.playlist.append(title)

    def remove_song(self):

        self.show_playlist()
        choice = int(input("Vilken låt ska bort?: "))
        self.playlist.remove(choice - 1)

        print("Success!")
    
    def __str__(self):
        return self.name

my_playlist = Playlist("Oktober 2025")


