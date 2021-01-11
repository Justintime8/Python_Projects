import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('spotifydb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    addedDate DATE
); ''')


fname = input('Enter file name: ')
if(len(fname) < 1 ) : fname = 'spotify_lib.xml'

stuff = ET.parse(fname)
all = stuff.findall('track')
for a in all :
    title = a.find('title').text
    artist = a.find('artist').text
    album = a.find('album').text
    addedDate = a.find('addedDate').text

    print(title, artist, album, addedDate)

    cur.execute(''' INSERT or IGNORE INTO Artist (name) VALUES (?)''', (artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ?)''', (album, artist_id) )
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ) )
    album_id = cur.fetchone()[0]

    cur.execute(''' INSERT OR REPLACE INTO Track (title, album_id, addedDate ) VALUES ( ?, ?, ?)''', ( title, album_id, addedDate) )

    conn.commit()
