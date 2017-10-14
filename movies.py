import media
import fresh_tomatoes
aa=media.Movie("Aashiqui 2",
               "",
               "https://upload.wikimedia.org/wikipedia/en/f/f3/Aashiqui_2_%28Poster%29.jpg",
               "https://www.youtube.com/watch?v=FyXXgpPqe6w")
nineteen=media.Movie("1920 The Evil Returns",
                     "",
               "https://upload.wikimedia.org/wikipedia/en/e/e7/1920_Evil_Returns_poster.jpg",
               "https://www.youtube.com/watch?v=Hq-U6HWZjsY")
fault=media.Movie("The Fault In Our Stars",
                  "",
                  "https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png",
                  "https://www.youtube.com/watch?v=9ItBvH5J6ss")
conjuring=media.Movie("The Conjuring",
                      "",
               "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
               "https://www.youtube.com/watch?v=k10ETZ41q5o")

movies=[aa,nineteen,fault,conjuring]
fresh_tomatoes.open_movies_page(movies)
