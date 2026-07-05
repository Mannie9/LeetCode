class Solution(object):
    def isPalindrome(self, x):
        temp = str(x)
        test = []
        check = []
        check.append(temp[0])
        for i in temp:
            test.append(i)
        for i in range(1, len(temp)):
            check.insert(0, temp[i])

        if check == test:
            return True
        else:
            return False

