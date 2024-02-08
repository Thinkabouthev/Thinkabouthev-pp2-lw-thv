from exercise import movies

def average_IMDB(names):
    sum=0
    for movie in movies:
        for name in names:
            if movie['name'] == name:
                sum += movie['imdb']

    print(sum/len(names))
    
print(average_IMDB(list(map(str,input().split())))) 