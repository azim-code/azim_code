
For authenticating use

username :- admin
password :- admin


#For listing genre
https://imdbprojectapi.herokuapp.com/api/genre/

# fro creating genre
https://imdbprojectapi.herokuapp.com/api/genre/
body {
"name":"Horror"
}

# for update genre
https://imdbprojectapi.herokuapp.com/api/genre/id
body {
"name":"thriller"
}

for delete genre
https://imdbprojectapi.herokuapp.com/api/genre/id




#For listing movies
https://imdbprojectapi.herokuapp.com/api/movies/

# fro creating movies
https://imdbprojectapi.herokuapp.com/api/movies/
    {
        "name": "Star wars",
        "popularity": 83.0,
        "imdb_score": 5.0,
        "genre": [
            1,
            2
        ],
        "director":"hello"
    }

# for update movies
https://imdbprojectapi.herokuapp.com/api/movies/id
    {
        "name": "Star wars",
        "popularity": 83.0,
        "imdb_score": 5.0,
        "genre": [
            1,
            2
        ],
        "director":"hello"
    }

for delete movies
https://imdbprojectapi.herokuapp.com/api/movies/id