class Solution:

    def encode(self, strs):

        answer = ""

        for i in strs:
            answer += str(len(i)) + "#" + i

        return answer

    def decode(self, s):

        answer = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            answer.append(s[j+1:j+1+num])
            i = j + 1 + num

        return answer
    
newsol = Solution()

# test = ["neet","code","love","you"]
test = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]

if (newsol.decode(newsol.encode(test)) == test):
    print("Test Passed!")
else:
    print("Test Failed!")