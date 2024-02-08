from exercise import movies

def average_categ(category):
    sum=0
    cnt=0
    for movie in movies:
            if movie['category'] == category:
                sum += movie['imdb']
                cnt += 1

    return sum/cnt
    
    
print(average_categ(input()))