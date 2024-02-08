from exercise import movies

def cateegory(cat):
    for movie in movies:
        if movie['category'] == cat:
            print(movie['name'])

cat = input()
cateegory(cat)
