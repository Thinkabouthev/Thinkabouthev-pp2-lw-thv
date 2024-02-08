def spy_game(nums):
    zeros = 0
    for i in nums:
        if zeros >= 2 and i == 7:
            return True
        elif i == 0:
            zeros += 1
    return False

print(spy_game(list(map(int,input().split()))))