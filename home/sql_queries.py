# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays (songplay_id int\
                                     ,start_time bigint\
                                     ,user_id int\
                                     ,level varchar\
                                     ,song_id varchar\
                                     ,artist_id varchar\
                                     ,session_id varchar\
                                     ,location text\
                                     ,user_agent text);
""")

user_table_create = ("""
create table if not exists users (user_id int\
                                 ,first_name varchar\
                                 ,last_name varchar\
                                 ,gender varchar\
                                 ,level varchar);
""")

song_table_create = ("""
create table if not exists songs (song_id varchar\
                                 ,title varchar\
                                 ,artist_id varchar\
                                 ,year int\
                                 ,duration decimal);
""")

artist_table_create = ("""
create table if not exists artists (artist_id varchar\
                                   ,name varchar\
                                   ,location text\
                                   ,latitude decimal\
                                   ,longitude decimal);
""")

time_table_create = ("""
create table if not exists time (start_time timestamp\
                                ,hour int\
                                ,day int\
                                ,week int\
                                ,month int\
                                ,year int\
                                ,weekday int);
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
insert into users (user_id, first_name, last_name, gender, level) values (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
insert into songs (song_id, title, artist_id, year, duration) values (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location, latitude, longitude) values (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
insert into time (start_time, hour, day, week, month, year, weekday) values (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
select c.song_id, c.artist_id from (select a.song_id, b.artist_id, a.title, b.name, a.duration from songs a join artists b on a.artist_id = b.artist_id)c where c.title = %s and c.name = %s and c.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]