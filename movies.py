class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.rating = None

    def set_rating(self, rating):
        if 1 <= rating <= 10:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 1 and 10")

    def __str__(self):
        return f"{self.title} ({self.genre}): {self.rating}"

class User():
    def __init__(self, user_name, movies=None, fav_genres=None):
        self.user_name = user_name
        self.movies = [] if movies is None else movies
        self.fav_genres = [] if fav_genres is None else fav_genres

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_fav_genre(self, genre):
        self.fav_genres.append(genre)


def get_movies():
    movies = []
    while True:
        title = input("Enter a movie title (or 'Done' to finish): ")
        if title == "Done":
            break
        genre = input(f"Enter a genre for '{title}': ")
        movies.append(Movie(title, genre))
    return movies

def ranking():
    movies = get_movies()
    for movie in movies:
        while True:
            try:
                rating = int(input(f"Rate the movie '{movie.title}' (1-10): "))
                movie.set_rating(rating)
                break
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 10.")
    return movies

def get_average_rating(rated_movies):
    return sum(m.rating for m in rated_movies) / len(rated_movies)

def get_highest_rating(rated_movies):
    return max(rated_movies, key=lambda m: m.rating)

def get_lowest_rating(rated_movies):
    return min(rated_movies, key=lambda m: m.rating)

def statistic(rated_movies):
    # ANSI colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RESET = '\033[0m'

    avg = get_average_rating(rated_movies)
    highest = get_highest_rating(rated_movies)
    lowest = get_lowest_rating(rated_movies)

    print("\nStatistics:")
    print(f"{ORANGE}Average rating: {avg:.2f}{RESET}")
    print(f"{GREEN}Highest rated movie: {highest.title} ({highest.rating}){RESET}")
    print(f"{RED}Lowest rated movie: {lowest.title} ({lowest.rating}){RESET}")

def recommendation_by_genre(rated_movies, genre):
    filtered = [m for m in rated_movies if m.genre.lower() == genre.lower()]
    if not filtered:
        print(f"No movies found in genre '{genre}'.")
        return None
    best = max(filtered, key=lambda m: m.rating)
    print(f"\nRecommended movie in genre '{genre}': {best.title} ({best.rating})")
    return None

def main():
    # Main
    rated_movies = ranking()
    rated_movies = [m for m in rated_movies if m.rating is not None]

    statistic(rated_movies)

    # Optional: Ask for a genre recommendation
    genre_input = input("\nEnter a genre for recommendation: ")
    recommendation_by_genre(rated_movies, genre_input)

if __name__ == "__main__":
    main()

