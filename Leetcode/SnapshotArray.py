class SnapshotArray:

    def __init__(self, length: int):
        self.current_arr = [0] * length
        self.snap_arr = []
        self.size = length

    def set(self, index: int, val: int) -> None:
        if index-1 < self.size:
            self.current_arr[index] = val
        else:
            raise Exception("Index out of bound")

    def snap(self) -> int:
        snap_len = len(self.snap_arr)
        self.snap_arr.append(self.current_arr.copy())
        return snap_len

    def get(self, index: int, snap_id: int) -> int:
        if snap_id < len(self.snap_arr):
            return self.snap_arr[snap_id][index]
        else:
            return 0

# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(4)
obj.set(0,8)
obj.set(2,5)
obj.set(3,2)
param_2 = obj.snap()
obj.set(2,20)
obj.set(0,14)
param_3 = obj.get(3,0)
obj.set(0,14)

# Memory limit is exceeding for bigger array in leetcode, mean you have to optimize it.
