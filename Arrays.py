#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
#Example 1:
#Input: [1,2,3,1]
#Output: true
#Example 2:
#Input: [1,2,3,4]
#Output: false

#As usual we'll get the naive approach out of the way first.

def brute_force_duplicate_search(array): # using a method to input an array into the method 
    for i in range(len(array) -1): #len is use to find the length of an array and this for loop is showing us a decrementing for loop
        for j in range(i+1,len(array)): #another for loop so it is showing us a double for loop to comapre one element to the other elements
            if array[i] == array[j]:
                if array[i] == array[j]:
                    return True
    return False
array = [1,2,46,32,98,61,36,33]
print(brute_force_duplicate_search(array))

#In Python we only have dynamic arrays
#Some basic operations and their complexities are given below :

#Look-up/Accses - O(1)
#Push/Pop - O(1)*
#Insert - O(n)
#Delete - O(n)

#append(something goes here) adds it to the end of the array in O(1)
array.append(45)

#In some special cases, the append(push) operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
#So when an element is to appended and the array is filled, the entire array has to be copied to a new locationMt Shasta, California 96067sha
#With more space allocated(generally double the space) this time so that more items can be appended.
#Therefore, some individual operations may reuire O(n) time or greater, but when averaged over a large number of operations,
#The complexity can be safely considered to be O(1)

#array pop method allows to remove the last element in the array in O(1)

array.pop()

print(array)

#INSERT
#INSERT operation is used to insert element in the beginning or at a specific location
#Operation is O(N) since after inserting the element at the desired location,
#The elements to the right of the array have to be updated with the correct index as they all have shifted by one place.
#This requires looping through the array. Hence, O(n) time.

array.insert(0,50) #inserts 50 at the beginning of the arrat and shifts all other elements one placew towards right O(n)    

array.insert(4,0) #inserts 0 at the index 4 thus shifting all elements starting from index4 one place towards right O(n)


#DELETE
#Similar to insert, it deletes an element from the specified location in O(n) time
#The elements to the right of the deleted element have to shifted one space left, which requires looping over the entire array
#Hence, O(n) time complexity
array.pop(0) 
#This pops the first element of the array, shifting the remaining elements of the array one place left. O(n)
print(array)

 #This command removes the first occurence of the element 17 in the array, for which it needs to traverse the entire array, which requires O(n) time
print(array)
del array[2:4]
 #This command deletes elements from position 2 to position 4, again, in O(n) time
print(array)

#contains duplicate 

#we will find the duplicate in array

#brute force method

def brute_force(array1):
    for i in range(len(array)-1): # different ways to iterate though a array 
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                return True
    return False

#practice 

def count_ones(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                return False
    return False


array1 =[1,2,3,4,4]
print(brute_force(array1))
print(count_ones(array1))