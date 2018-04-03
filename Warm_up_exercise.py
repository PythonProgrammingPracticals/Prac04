

numbers = [3, 1, 4, 1, 5, 9, 2]
print("3")
#prints value of = 3

print(numbers[0])
#prints value of = 2

print(numbers[-1])
#prints vaue of = 1

print(numbers[3])
#prints value of = [3, 1, 4, 1, 5, 9,]

print(numbers[:-1])
#prints value of = [1]

print(numbers[3:4])
#prints value of = [True]

print(5 in numbers)
#prints = False

print(7 in numbers)
#prints = False

print("3" in numbers)
#prints = [3,1,4,1,5,9,2,6,5,3]

print(numbers + [6, 5, 3])

# A. Change first element in numbers to 10
numbers [0] = 10
print(numbers)

# B. Change last element in numbers to 1
numbers[len(numbers)-1] = 1
print(numbers)

# C. Get all the elements from numbers except first two
print(numbers[2:len(numbers)])

# D. Check if 9 is an element
print (9 in numbers)


