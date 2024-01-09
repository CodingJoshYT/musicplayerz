import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
from mutagen.mp3 import MP3
import sys

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x300")

        self.playlist = []
        self.current_song_index = 0

        self.initialize_gui()
        self.initialize_player()

    def initialize_gui(self):
        self.song_var = tk.StringVar()
        self.song_label = tk.Label(self.root, textvariable=self.song_var, font=("Helvetica", 12))
        self.song_label.pack(pady=10)

        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="lightgrey", selectbackground="darkblue")
        self.playlist_box.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Add Songs", command=self.add_songs)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_song)
        self.next_button.pack(side=tk.LEFT, padx=10)

    def initialize_player(self):
        pygame.mixer.init()

    def add_songs(self):
        songs = filedialog.askopenfilenames(title="Select Songs", filetypes=[("MP3 Files", "*.mp3")])
        if songs:
            self.playlist.extend(songs)
            self.update_playlist_box()

    def update_playlist_box(self):
        self.playlist_box.delete(0, tk.END)
        for song in self.playlist:
            self.playlist_box.insert(tk.END, os.path.basename(song))

    def play_music(self):
        if self.playlist:
            song_path = self.playlist[self.current_song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

            song_length = MP3(song_path).info.length
            self.song_var.set(f"Now Playing: {os.path.basename(song_path)} ({self.format_time(song_length)})")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.song_var.set("Music Stopped")

    def next_song(self):
        if self.playlist:
            self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
            self.play_music()

    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes:02d}:{seconds:02d}"

def is_executable():
    return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

if __name__ == "__main__":
    if is_executable():
        root = tk.Tk()
        music_player = MusicPlayer(root)
        root.mainloop()
    else:
        messagebox.showinfo("Alert", "Please run the Music Player installer and select the music file to start.")
