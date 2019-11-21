from math import floor

class complHeap: # 即便使用蛮力算法而不是Floyd算法进行建堆，整个算法的排序过程复杂度仍为O（nlogn）
                # 其高运行效率、低开发成本，以及低资源消耗等诸多优点的完美结合，若离开二叉堆这一精巧的数据结构，确实是难以想象。
    elems = []

    def __init__(self, elems) -> None:
        self.elems = elems
        self.heapify(len(self.elems))

    def percolateDown(self, i, n): # 下滤，n表示二叉堆的范围为elems[0,n]
        while self.LChild(i) <= n or self.RChild(i)<= n: # i元素仍有孩子
            if self.RChild(i) > n: # 若i元素只有左孩子
                index = self.LChild(i)
            else:
                if self.elems[self.LChild(i)] > self.elems[self.RChild(i)]: # 选出左右孩子的最大者
                    index = self.LChild(i)
                else:
                    index = self.RChild(i)
            if self.elems[i] > self.elems[index]:
                break
            else:
                self.elems[i], self.elems[index] = self.elems[index], self.elems[i] # 此处可进行常数意义下的改进
                i = index
        return i

    def percolateUp(self, i): # 上滤
        while i > 0 and self.elems[i]>self.elems[self.Parent(i)]:
            self.elems[i], self.elems[self.Parent(i)] = self.elems[self.Parent(i)], self.elems[i] # 此处可以进行常系数意义上的改进
            i = self.Parent(i)
        return i # 返回上滤最终抵达的位置

    def heapify(self, n): #Floyd建堆算法
        # for i in range(1, n):
        #     self.percolateUp(i) # 蛮力算法，按照层次遍历次序逐一经上滤插入各节点
        for i in range(self.LastInternal(n), -1, -1):
            self.percolateDown(i, len(self.elems) - 1)

    def heapSort(self): # 就地堆排序，除了交换操作需要常数个辅助空间以外，我们并不需要更多的辅助空间
        for i in range(len(self.elems) - 1,0,-1):
            self.elems[0], self.elems[i] = self.elems[i], self.elems[0]
            self.percolateDown(0, i - 1)

    def Parent(self, i):
        return floor((i-1)/2)

    def LChild(self, i):
        return 1+i*2 # 奇数

    def RChild(self, i):
        return (1+i)*2 # 偶数

    def LastInternal(self, n): # 最后一个内部节点，即末节点的父亲
        return self.Parent(n - 1)

    def insert(self, T): # 插入的核心在于上滤
        self.elems.append(T)
        self.percolateUp(len(self.elems) - 1)

    def getMax(self):
        return self.elems[0]

    def delMax(self):
        maxElem  = self.elems[0] #备份被删除的最大元素
        self.elems[0] = self.elems[-1] # 高处不胜寒
        self.elems.pop()
        self.percolateDown(0, len(self.elems) - 1)
        return maxElem # 返回此前备份的最大元素

if __name__ == '__main__': # 用于测试
    A = [3,2,33,4,45,3,231,323,43,243,432,324,234,4,32,423,432,234,55,99999999]
    complHeap1 = complHeap(A)
    A = []
    for i in range(len(complHeap1.elems)): # 时间复杂度为O（nlogn），但还可以在空间复杂度的意义下进行改进
        A.insert(0,complHeap1.delMax())
    print(A)

    A = [3,2,33,4,45,3,231,323,43,243,432,324,234,4,32,423,432,234,55,99999999]
    complHeap2 = complHeap(A)
    complHeap2.heapSort()
    print(complHeap2.elems)


