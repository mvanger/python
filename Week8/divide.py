# # Divide and conquer algorithms
# # mergesort, quicksort

# def partition(l, i ,j):
#   pivot = l[0]
#   while True:
#     while l[i] < pivot:
#       i += 1
#     while l[j] > pivot:
#       j -= 1
#     if j <= i:
#       return j
#     l[i], l[j] = l[j], l[i]
#     i += 1
#     j -= 1
#   return l

# def quicksort(l, i, j):
#   if i == j:
#     return
#   q = partition(l, i, j)
#   quicksort(l, i, q)
#   quicksort(l, q + 1, j)

# def qsort1(list):
#   if list == []:
#     return []
#   else:
#     pivot = list[0]
#     lesser = qsort1([x for x in list[1:] if x < pivot])
#     greater = qsort1([x for x in list[1:] if x >= pivot])
#     return lesser + [pivot] + greater

# a = [7,6,3,5,1,10,12]
# # print(quicksort(a, 0, len(a) - 1))

# def max(l):
#   max = l[0]
#   for e in l:
#     if e > max:
#       max = e

# def k_max(l, k):
#   if len(l) < k:
#     return l
#   max = l[0:k]
#   quicksort(max, 0, k-1)
#   for x in l[k:]:
#     p = 0
#     while x < max[p]:
#       pass







