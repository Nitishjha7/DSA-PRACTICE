#generate all subarray from given array 

def sub_array(arr):
    n=len(arr)

    for i in range(n):#this loop decide where to start 
        for j in range(i,n):#this loop decide what the end point
            for k in range(i,j+1):#this loop print value 
                print(arr[k],end=" ")
            print()

arr=[1,2,4,5,6,7]
sub_array(arr)
#formaula for calculating no of subarray n(n+1)2
#here i is 0,1,2,3,4,5
#so if i is 0 then j is bw 0 to 5 
#so if i is 0 and j is o then k is o to o it will print 1 
#and when i is 0 and j is 1 then k is o to 1 it will print 1 2

#we can use  print(arr[i:j+1]) this at palce of third loop ye interalay python slicing se kar dega 