class NestedIterator(object):

    def __init__(self, nestedList):
        self.arr = []
        self.i = 0
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for x in nestedList:
            if x.isInteger():
                self.arr.append(x.getInteger())
            else:
                self.flatten(x.getList())

    def next(self):
        ans = self.arr[self.i]
        self.i += 1
        return ans

    def hasNext(self):
        return self.i < len(self.arr)