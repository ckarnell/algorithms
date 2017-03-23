def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i+=1
            else:
                alist[k]=righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j+=1
            k+=1

if __name__ == "__main__":
    import unittest
    class MergeSortTest(unittest.TestCase):
        def test_merge_sort(self):
            inputs = ([54,26,93,17,77,31,44,55,20], [])
            for result in inputs:
                mergeSort(i)
                expected = sorted(i)
                self.assertTrue(result == expected)

        unittest.main()
