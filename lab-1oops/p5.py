numbers = [4, 8, 15, 16, 23, 42]

def stats(nums):
    low = min(nums)
    high = max(nums)
    average = sum(nums) / len(nums)
    return low, high, average

lo, hi, avg = stats(numbers)
print(lo, hi, avg)

def grade(marks, passing=50):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"

print(grade(55))
print(grade(55, passing=60))