class MyHashMap:

    def __init__(self):
        self.obj = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.obj[key] = value

    def get(self, key: int) -> int:
        if self.obj[key] != -1:
            return self.obj[key]
        else:
            return -1
    def remove(self, key: int) -> None:
        self.obj[key] = -1
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)