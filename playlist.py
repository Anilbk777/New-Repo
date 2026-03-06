from typing import List
class Song:
  def __init__(self, name: str):
    self.name = name

  def __repr__(self):
    return f"Song(name = {self.name})"

class Playlist:
  def __init__(self, name: str):
    self.name = name
    self.__songs: List[Song]  = []

  def add_song(self, song: Song):
    if song in self.__songs:
      raise ValueError("Song already exist in this playlist")
    self.__songs.append(song)

  def remove_song(self, song: Song):
    if song not in self.__songs:
      raise ValueError("Song is not in the Playlist")
    self.__songs.remove(song)

  @property
  def song(self):
    return list(self.__songs)

  def __repr__(self):
    return f"Playlist(name={self.name}, songs={self.song})"



if __name__ =="__main__":
  song1 = Song("Thamana haat yoo")
  song2 = Song("aau timi yo jindagi ma")

  playlist1 = Playlist("Love songs")

  playlist1.add_song(song1)
  playlist1.add_song(song2)

  # print(playlist1)

  song3 = Song("lalu patay nugyo vui tire")
  playlist1.add_song(song3)

  print(playlist1)

  playlist1.remove_song(song3)

  print(playlist1)



