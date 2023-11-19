def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
    return A
def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i + 1

if __name__ == "__main__":
    A = [2,8,7,1,3,5,6,4]
    QuickSort(A,0,len(A)-1)
    print(A) # [1,2,3,4,5,6,7,8]
    print("The array above should be [1,2,3,4,5,6,7,8].")