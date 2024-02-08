#function1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input())
print(grams_to_ounces(grams))