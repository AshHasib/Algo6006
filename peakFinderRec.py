

def peakFinder(A, start, end):
    mid=(start+end+1)//2
    
    if (A[mid]>A[mid+1]) and mid is start:
        return A[mid]
        
    elif(A[mid>A[mid-1]]) and mid is end:
        return A[mid]
        
    elif(A[mid]>A[mid+1] ) and (A[mid]>A[mid-1]):
        return A[mid]
        
    elif(A[mid]<A[mid-1]):
        return peakFinder(A, start, mid-1)
        
    elif(A[mid]<A[mid+1]):
        return peakFinder(A, mid+1, end)

A=[5, 7, 8, 4, 3, 1, -1]

print('The peak value is :', end=' ')
print (peakFinder(A, 0, 6))
