from Robot_origin import Solution

test1 = 'UDG'  
test2 =  ""     
test3 = "RRRRRUDLLL" 
test4 = "DDD"  
test5 = 'DDRRLLUU'

robot = Solution()

print('test3', robot.judgeCircle(test3))  # False
print('test4', robot.judgeCircle(test4))  # False
print('test5', robot.judgeCircle(test5))  # True

# comment the next line if you want to check for test2
print('test1', robot.judgeCircle(test1)) # expect an error on the letter G
print('test2', robot.judgeCircle(test2)) # expect an error of length of moves out of range