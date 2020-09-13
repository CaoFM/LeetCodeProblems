#--------------------------------------#
#              Problem                 #
#--------------------------------------# 

# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

# Example:

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version. 

#--------------------------------------#
#              Solution                #
#--------------------------------------# 


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # start at 0, n+1 instead of 1,n to cover all good or all bad cases
        good = 0
        bad = n+1

        while bad - good > 1:
            test = (good + bad) // 2
            if isBadVersion(test):
                bad = test
            else:
                good = test
            
        return bad


#--------------------------------------#
#              Test Code               #
#--------------------------------------# 

# API missing

# if __name__ == '__main__':
    
#     inputs = [[12,345,2,6,7896],[555,901,482,1771]]
#     answers = [2,1]

#     s = Solution()

#     for i in range(len(inputs)):
#         output = s.findNumbers(inputs[i])
#         print(output)
#         if output != answers[i]:
#             print('wrong answer. expecting: '+str(answers[i]))