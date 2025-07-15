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
        return f"{self.title}: {self.rating}"

def get_movies():
    movies = []
    user_input = input("Enter a movie title (or 'Done' to finish): ")
    while user_input != "Done":
        movies.append(Movie(user_input))
        user_input = input("Enter a movie title (or 'Done' to finish): ")
    return movies

def ranking():
    movies = get_movies()
    for movie in movies:
        while True:
            try:
                user_rank = int(input(f"Rank the movie '{movie.title}' (1-10): "))
                movie.set_rating(user_rank)
                break
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 10.")

    print("\nMovie Rankings:")
    for movie in movies:
        print(movie)

    # to check if there is a movie note rated
    rated_movies = [m for m in movies if m.rating is not None]

    avg = sum(m.rating for m in rated_movies) / len(rated_movies)
    highest = max(rated_movies, key=lambda m: m.rating)
    lowest = min(rated_movies, key=lambda m: m.rating)

    # ANSI colors
    RED = '\033[91m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RESET = '\033[0m'

    print("\nStatistics:")
    print(f"{ORANGE}Average rating: {avg:.2f}{RESET}")
    print(f"{GREEN}Highest rated movie: {highest.title} ({highest.rating}){RESET}")
    print(f"{RED}Lowest rated movie: {lowest.title} ({lowest.rating}){RESET}")

ranking()
