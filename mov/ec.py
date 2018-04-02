import fresh_tomatoes
import media
liberal_arts = media.Movie("Liberal Arts",
                           "When 30-something Jesse returns to his alma mater for a professor's retirement party, .... I see this movie as a look at life through the perspectives of different generations.",
                           "http://www.impawards.com/2012/posters/liberal_arts_ver2.jpg",
                           "https://www.youtube.com/watch?v=BqIuv_JX5wM")

#print(liberal_arts.storyline)

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "Joel and Clementine begin a relationship post a train journey together, unaware that they had previously been in a relationship, the memories of which were clinically erased.",
                               "http://www.gstatic.com/tv/thumb/movieposters/33409/p33409_p_v8_ae.jpg",
                               "https://www.youtube.com/watch?v=1GiLxkDK8sI")

dead_poets_society = media.Movie("Dead Poets Society",
                                 "John Keating, a progressive English teacher, encourages his students to break free from the norms, go against the status quo and live unapologetically.",
                                 "http://t1.gstatic.com/images?q=tbn:ANd9GcSFiizcraYyxtIB2imVhFaWB5eMW1m95_Hp42MVj8Ngxo3Eq386",
                                 "https://www.youtube.com/watch?v=wrBk780aOis")
love_actually  = media.Movie("Love Actually",
                             "Eight London couples try to deal with their relationships in different ways. Their tryst with love makes them discover how complicated relationships can be.",
                             "http://img.moviepostershop.com/love-actually-movie-poster-2003-1020189066.jpg",
                             "https://www.youtube.com/watch?v=KdzH6a-XEGM")
her = media.Movie("HER",
                  "Theodore is a lonely letter writer and loves playing video games. His life takes a leap when he decides to buy a new software advertised as the world's first artificially intelligent operating system.",
                  "http://t2.gstatic.com/images?q=tbn:ANd9GcTJM7K3IleZaH3U-CDfARoFdfpB3Atg8pQqIgRkdlkAQHdMjBYH",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

notebook = media.Movie("The Notebook",
                       "Duke reads the story of Allie and Noah, two lovers who were separated by fate, to Ms. Hamilton, an old woman who suffers from Alzheimer's, on a daily basis out of his notebook.",
                       "http://www.gstatic.com/tv/thumb/movieposters/33410/p33410_p_v8_aa.jpg",
                       "https://www.youtube.com/watch?v=7ifs0rMLMlQ")

movies = [liberal_arts,eternal_sunshine,dead_poets_society,love_actually,her,notebook]
fresh_tomatoes.open_movies_page(movies)
