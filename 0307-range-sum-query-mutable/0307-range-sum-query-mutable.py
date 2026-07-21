class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, nums)

    # Build Segment Tree
    def build(self, node, start, end, nums):
        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2

        self.build(2 * node + 1, start, mid, nums)
        self.build(2 * node + 2, mid + 1, end, nums)

        self.tree[node] = (
            self.tree[2 * node + 1] +
            self.tree[2 * node + 2]
        )

    # Update
    def update(self, index, val):
        self.updateTree(0, 0, self.n - 1, index, val)

    def updateTree(self, node, start, end, index, val):

        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2

        if index <= mid:
            self.updateTree(2 * node + 1,
                            start,
                            mid,
                            index,
                            val)
        else:
            self.updateTree(2 * node + 2,
                            mid + 1,
                            end,
                            index,
                            val)

        self.tree[node] = (
            self.tree[2 * node + 1] +
            self.tree[2 * node + 2]
        )

    # Query
    def sumRange(self, left, right):
        return self.query(0, 0, self.n - 1, left, right)

    def query(self, node, start, end, left, right):

        # No overlap
        if right < start or end < left:
            return 0

        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2

        return (
            self.query(2 * node + 1,
                       start,
                       mid,
                       left,
                       right)
            +
            self.query(2 * node + 2,
                       mid + 1,
                       end,
                       left,
                       right)
        )