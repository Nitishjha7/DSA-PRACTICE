#find  element  largest in array 

#sort the array in ascending order and print last index element (size of array -1)

#brute force 
def largest_Arr(arr):
    arr.sort()
    return arr[-1]

if __name__=="__main__":
    arr1=[1,23,54,5,6,7]
    arr2=[24,6,8,8,4,]

    print("largest element in the array is" ,largest_Arr(arr1))
    print("largest element in the array is" ,largest_Arr(arr2))


#find the largest element and its index

def largestarr(arr):
    if not arr:
        return None,None
    
    max_val=arr[0]
    max_idx=0

    for i in range(1,len(arr)):
        if arr[i] > max_val:
            max_val=arr[i]
            max_idx=i
    return max_val,max_idx    

if __name__=="__main__":
    arr3=[2,46,7,9,0,111]
    arr4=[1,5,8,9,4,46]

    val,idx=largestarr(arr3)
    print("largest element",val,'at index',idx)

    val,idx=largestarr(arr4)
    print("largest element",val,'at index',idx)#this is the best approach Time Complexity: O(N), where N is the size of the array, as we are iterating through the array once.
