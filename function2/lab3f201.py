from exercise import movies

def single(name):
    for movie in movies:
        if name == movie["name"] and movie["imdb"] > 5.5:
            return True
    return False

print(single(input())) 