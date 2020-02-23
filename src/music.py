import pygame


class Music:
    """A class to play music and sounds"""
    def __init__(self):
        self.music_file = 'resources/theme.wav'
        self.pop_sound = pygame.mixer.Sound('resources/Pop.wav')
        self.thunk_sound = pygame.mixer.Sound('resources/thunk.wav')
        pygame.mixer.pre_init(44100, -16, 2, 2048)  # Setup to avoid sound lag
        pygame.mixer.init()
        pygame.mixer.music.load(self.music_file)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.rewind()
        pygame.mixer.music.pause()

    def start_music(self):
        pygame.mixer_music.unpause()

    def pop_sound_effect(self):
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(self.pop_sound)
        pygame.mixer.music.unpause()

    def thunk_sound_effect(self):
        pygame.mixer.music.pause()
        pygame.mixer.Sound.play(self.thunk_sound)
        pygame.mixer.music.unpause()
