from exercise import movies

def films():
    list = []
    for movie in movies:
        if movie['imdb'] >= 5.5:
            list.append(movie['name'])

    return list

print(films())