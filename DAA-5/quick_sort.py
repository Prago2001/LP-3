import random


class QuickSort:
    def __init__(self,array):
        self.array = array
    

    # Deterministic method to find pivot
    def partition(self,low,high):
        # High element is default pivot
        pivot = self.array[high]

        # pointer for greater element
        i = low - 1


        for j in range(low,high):
            if self.array[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i += 1
                self.array[i],self.array[j] = self.array[j],self.array[i]
        # swap the pivot element with the greater element specified by i
        self.array[i+1],self.array[high] = self.array[high],self.array[i+1]

        return i+1
    
    def partition_random(self,low,high):
        pivot = random.randint(low,high)
        self.array[pivot],self.array[high] = self.array[high],self.array[pivot]
        return self.partition(low,high)
    
    # deterministic variant of sort
    def sort_d(self,low,high):
        if low < high:

            pivot = self.partition(low,high)
            self.sort_d(low,pivot-1)
            self.sort_d(pivot+1,high)
    
    
    # random variant of sort
    def sort_r(self,low,high):
        if low < high:
            pivot = self.partition_random(low,high)
            self.sort_r(low,pivot-1)
            self.sort_r(pivot+1,high)


while True:
    print("Press Ctrl+C to exit...")
    array = [int(i) for i in input("Enter array").split(" ")]
    print("Deterministic variant of sort")
    sort1 = QuickSort(array)
    sort1.sort_d(0,len(array)-1)
    print(sort1.array)
    print("Radomized variant of sort")
    sort2 = QuickSort(array)
    sort2.sort_r(0,len(array)-1)
    print(sort2.array)
    
