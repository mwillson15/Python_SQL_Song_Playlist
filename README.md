# Python_SQL_Song_Playlist
This repository contains files for a project which integrates Python and SQL to build a song playlist. The "Python_SQL_Song_Playlist" folder contains 5 files related to the project.

## Objectives
- Practice integrating Python and SQL programming
- Practice modeling a relational database

## Motivations
This was one of the final projects in a Python specialization I completed which aimed to apply many of the topics taught throughout the specialization including Python/SQL programming and modeling relational databases.

## Reading Through Files
Below are descriptions of the project files in the order you should go about reading them.

### "Song_Playlist_env_requirements.txt"
This is a text file containing the requirements for the virtual environment used for this project. Note, the "sqlite3" module used in this project requires SQLite 3.14.2 or newer.

### "tracks.csv"
This is a CSV file containing the song data used in "Playlist_Code.py".

### "Playlist_Code.py"
This is a Python script file containing the code that constructs a song playlist as a SQLite relational database. The script integrates Python and SQL to parse the song data from "tracks.csv" and executes SQL queries to model a relational database with these data.

### "Track_DB.sqlite"
This is a SQLite database file containing the database that is created by the "Playlist_code.py" program and is modified by "Playlist_code.py" with each run of the program.

### "Track_DB_copy.sqlite"
This is a SQLite database file containing a copy of the database that was created by "Playlist_code.py" and is not modified by the program.

