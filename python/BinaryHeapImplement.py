# Binary Heap implementation
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      print(self.heapList) # add the print() to check the heapList
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      print(self.heapList) # add the print() to check the heapList
      self.percDown(1)
      return retval


    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
      return()

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])
# print(self.heapList)

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
# # output
# # 2
# # 3
# # 5
# # 6
# # 9

# Add print() result
# [0, 2, 3, 6, 5, 9]
# [0, 9, 3, 6, 5]
# 2
# [0, 3, 5, 6, 9]
# [0, 9, 5, 6]
# 3
# [0, 5, 9, 6]
# [0, 6, 9]
# 5
# [0, 6, 9]
# [0, 9]
# 6
# [0, 9]
# [0]
# 9