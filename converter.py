
##this module finds the max of some numbers


def high_number(numbers):
    high = numbers[0]
    for nums in numbers:
        if nums > high:
            high = nums
    return high