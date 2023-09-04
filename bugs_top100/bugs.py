import requests
from bs4 import BeautifulSoup

def get_songs():
  res = requests.get("https://music.bugs.co.kr/chart")
  soup = BeautifulSoup(res.text, "html.parser")
  tr_list = soup.select("table.byChart > tbody > tr")

  songs = []

  for rank, tr in enumerate(tr_list,1):
    song_no = tr.select_one("input")["value"]    # input이라는 tag안의 value값을 가져와라
    title_tag = tr.select_one("th > p > a")
    artist_tag = tr.select_one("td > p > a")
    album_tag = tr.select_one("td > .album")     # td에 클래스 album있으면 가져와라

    song = {
      "song_no": song_no,
      "title": title_tag.text,
      "artist": artist_tag.text,
      "album": album_tag.text
    }

    songs.append(song)

  return songs

if __name__ == "__main__":
  songs = get_songs()
  for song in songs:
    print(song)