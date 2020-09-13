# Given an array nums of integers, return how many of them contain an even number of digits.
 
# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

# Constraints:

#     1 <= nums.length <= 500
#     1 <= nums[i] <= 10^5

class Solution:
    def findNumbers(self, nums) -> int:
        def isEvenDigits(num):
            even_digit = False
            while (num // 10) > 0:
                even_digit = ~even_digit

                last_digit = num % 10
                num = (num - last_digit) / 10

            return even_digit

        count = 0
        for number in nums:
            if isEvenDigits(number):
                count += 1

        return count

if __name__ == '__main__':
    
    inputs = [[12,345,2,6,7896],[555,901,482,1771]]
    answers = [2,1]

    s = Solution()

    for i in range(len(inputs)):
        output = s.findNumbers(inputs[i])
        print(output)
        if output != answers[i]:
            print('wrong answer. expecting: '+str(answers[i]))