def sum_array(arr):
    n= len(arr)
    result=0

    for i in range(n):
        temp=0
        for j in range(i,n):
            temp +=arr[j]
            result +=temp
        return result
    
arr=[2,3,4,5]
print(sum_array(arr))
