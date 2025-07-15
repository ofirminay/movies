def get_moves():
    movies_list = []
    user_input = input('Enter a movie title: ')
    while user_input != "Done":
        movies_list.append(user_input)
        user_input = input('Enter a movie title: ')
    return movies_list

def ranking():
    rank = {}
    movies_list = get_moves()
    for movie in movies_list:
        user_rank = input(f'Rank the movie {movie}: ')
        if user_rank > 10 or user_rank < 1:
            print(f'The movie {movie} is out of range.')
            raise ValueError('The movie rank is out of range.')
        rank[movie] = user_rank
    return rank

print(ranking())

