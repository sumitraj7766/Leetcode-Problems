# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, interator):
        self.interator = interator

        if self.interator.hasNext():
            self.nextElement = self.interator.next()
        else:
            self.nextElement = None
       

    def peek(self):
        return self.nextElement
        

    def next(self):
        ans = self.nextElement

        if self.interator.hasNext():
            self.nextElement = self.interator.next()
        else:
            self.nextElement = None

        return ans
        
        

    def hasNext(self):
        return self.nextElement is not None
        
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].