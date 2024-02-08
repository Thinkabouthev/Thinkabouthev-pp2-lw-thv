def histogram():
    nums = input()
    nums = [int(num) for num in nums.split()] #строку в инт
    
    for i in range(len(nums)):
        print(nums[i] * '*')

histogram()