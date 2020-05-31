""" lists [] store a collection of data that are related as opposed to storing data as a separate variables.
    Iin python Individual values in list are accessible via their Indexes
    indexes start at 0 not 1, the last item in a list has an index of -1 """

userAge1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
userAge2 = [18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
            42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
age = userAge1[0]  # age has been assigned the value 1

''' Slicing 
    the notation [2:4] is a slice 
    in  python the start of the index is always included so 2 (is index 2)
    however the item on the end is always excluded so 4(0, 1,2,3,4) - 1 is 4  '''
print(userAge1[2:4])
''' here the slicing  will return a range index 2 to index 5 (-1)'''
print(userAge1[2:5])

''' Slicer - stepper 
    in this example the 3rd number is referred to as a stepper
    only ever 2nd (2) item from index 1 to 16 will be returned'''
print(userAge1[1:16:2])

''' slicer - default values 
    default value for the first no is 0, the example below will return [1,2]'''
print(userAge1[:2])
''' the default for the 2nd number is the last item on the index'''
print(userAge1[10:])

''' you can modify an index item by 
    1. assigning it a new value 
    2. deleting 
    3. adding a new item 
    '''
userAge1[0] = 0.5
del userAge1[0]
userAge1.append(1)

