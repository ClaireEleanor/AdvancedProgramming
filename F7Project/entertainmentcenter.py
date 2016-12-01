#!/usr/bin/python

import fresh_tomatoes
import media


godfather = media.Movie("The Godfather", "An offer you can't refuse.", "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

lebowski = media.Movie("The Big Lebowski", "The bums lost, Lebowski!", "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg", "https://www.youtube.com/watch?v=cd-go0oBF4Y")

whiplash = media.Movie("Whiplash", "Jazz, unraveled", "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg", "https://www.youtube.com/watch?v=7d_jQycdQGo")



movies = [godfather, lebowski, whiplash]

fresh_tomatoes.open_movies_page(movies)
