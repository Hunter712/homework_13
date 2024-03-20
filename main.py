import json
import os
import shutil
import csv

import datas as kek


def get_current_dir():
    return os.getcwd()


path_to_files_dir = f"{get_current_dir()}/genres"
if os.path.exists(path_to_files_dir):
    # usefull line for avoiding manual deleting dirs all the time
    shutil.rmtree(path_to_files_dir)

# task 1
genres = json.loads(kek.ganres)
# print(genres)

# task 2
path = os.path.join(get_current_dir(), "genres")
os.mkdir(path)
os.chdir(get_current_dir() + "/genres")

for each_genre in genres["results"]:
    os.mkdir(os.path.join(get_current_dir(), each_genre["genre"]))

# task 3
csv_data = [['title', 'year', 'rating', 'type', 'ganres']]

for each_genre in genres["results"]:
    os.chdir(get_current_dir() + f"/{each_genre['genre']}")

    with open(get_current_dir() + "/new.csv", 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_data)

    os.chdir("..")

# task 4
films_data = kek.films_data
for film in films_data:

    genres_for_each_film = [x["genre"] for x in film["gen"]]

    for film_genre in genres_for_each_film:
        os.chdir(get_current_dir() + f"/{film_genre}")

        with open(get_current_dir() + "/new.csv", 'a') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows([[film["title"], film["year"], film["rating"], film["type"], ';'.join(genres_for_each_film)]])

        os.chdir("..")



