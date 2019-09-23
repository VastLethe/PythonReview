
def swap(a, i, j):
  a[i], a[j] = a[j], a[i]
def maxHeap(a, n, max):
    while True:
        biggest = n
        c1 = 2 * n + 1
        c2 = c1 + 1
        for c in [c1, c2]:
            if c < max and a[c] > a[biggest]:
                biggest = c
        if biggest == n:
            return
        a[biggest], a[n] = a[n], a[biggest]
        n = biggest

def heapify(a):
  i = (len(a)- 1) / 2
  max = len(a)
  while i >= 0:
    maxHeap(a, i, max)
    i -= 1

def heapsort(a):
  heapify(a)
  j = len(a) - 1
  while j > 0:
    swap(a, 0, j)
    maxHeap(a, 0, j)
    j -= 1


alist = [54,26,93,17,77,31,44,55,20,10]
heapsort(alist)
print (alist)
