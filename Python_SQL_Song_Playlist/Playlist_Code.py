'''
Python_SQL_Song_Playlist Script 

This code is creating a multi-table relational database from a CSV file with playlist data in it. The database has multiple relationships between tables where these tables are eventually JOINED through these relationships at the end of the script.  
'''

import sqlite3

conn = sqlite3.connect('Track_DB.sqlite')
curr = conn.cursor()

#This code removes and creates tables with each run of the script.
curr.executescript('''DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track''')

curr.executescript('''CREATE TABLE Artist (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER, count INTEGER)''')

data_handle = open('tracks.csv')

#Loop to construct database from the "tracks.csv" file.
for line in data_handle: 
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7:
        continue
    
    track_data = pieces[0]
    artist_data = pieces[1]
    album_data = pieces[2]
    count_data = pieces[3]
    rating_data = pieces[4]
    length_data = pieces[5]
    genre_data = pieces[6]
    
    curr.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_data,))
    curr.execute('SELECT id FROM Artist WHERE name = ?',(artist_data,))
    artist_id = curr.fetchone()[0]
    
    curr.execute('INSERT OR IGNORE INTO Genre(name) VALUES (?)',(genre_data,))
    curr.execute('SELECT id FROM Genre WHERE name = ?', (genre_data,))
    genre_id = curr.fetchone()[0]
    
    curr.execute('INSERT OR IGNORE INTO Album (artist_id,title) VALUES (?,?)', (artist_id, album_data))
    curr.execute('SELECT id FROM Album WHERE title = ?', (album_data,))
    album_id = curr.fetchone()[0]
    
    curr.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)''', (track_data, album_id, genre_id, length_data, rating_data, count_data))
    
conn.commit()

#Query to join tables.
curr.execute('SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Artist JOIN Album JOIN Genre ON Track.album_id = Album.id AND Track.genre_id = Genre.id AND Album.artist_id = Artist.id')

conn.commit()
print('MUCH SUCCESS!!')




    
