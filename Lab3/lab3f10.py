nums=list(map(int, input().split()))

def unique(nums):
    output=[]
    for i in nums:
        if i not in output:
            output.append(i)
    print(output)

unique(nums)