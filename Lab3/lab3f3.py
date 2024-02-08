def solve(numheads, numlegs):
    chicken_num = (numlegs - numheads*2)/2
    rabbit_num = numheads - chicken_num
    return chicken_num, rabbit_num

numheads = int(input())
numlegs = int(input())
print("number of chickens and rabbits:", solve(numheads, numlegs))