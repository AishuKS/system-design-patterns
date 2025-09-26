class DVDPlayer:
    def on(self):
        print("DVD is on")
    def play(self, movie):
        print(f"DVD is playing movie : {movie}")

class Projector:
    def on(self):
        print("Projector is on")
    
    def wide_screen_mode(self):
        print("Projector in widescreen mode")

class SurroundSoundSystem:
    def on(self):
        print("Surround Sound is on")
    def set_volume(self, level):
        print(f"volumne set to {level}")

#Facade Class
class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, sound: SurroundSoundSystem):
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
    
    def watch_movie(self, movie, volume = 10):
        print("Get ready to watch movie")
        self.dvd.on()
        self.dvd.play(movie)
        self.projector.on()
        self.projector.wide_screen_mode()
        self.sound.on()
        self.sound.set_volume(volume)

dvd = DVDPlayer()
projector = Projector()
sound = SurroundSoundSystem()

home_theatre = HomeTheaterFacade(dvd, projector, sound)
home_theatre.watch_movie("Harry Potter")
home_theatre.watch_movie("Harry Potter", 50)