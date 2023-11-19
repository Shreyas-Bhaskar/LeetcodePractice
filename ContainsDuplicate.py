def containsDuplicate(nums):
    #Creating a data structure to store each element in array we scan through
    hash_table = {}
    #Going through each element in array
    for p in range(len(nums)):
        #If the current element is not in a data structure we created yet then append current element else we know that array is duplicated
        if hash_table.get(nums[p]):
            return True
        else:
            hash_table[nums[p]] = True
    return False
if __name__ == "__main__":
    print(containsDuplicate([1,2,3,1])) #True
    print(containsDuplicate([1,2,3,4])) #False
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) #True
    print(containsDuplicate([1,2,3,4,5,6,7,8,9,10])) #False
    print(containsDuplicate([1,1,1,1,1,1,1,1,1,1])) #True
    print("The booleans above should be True, False, True, False, and True.")