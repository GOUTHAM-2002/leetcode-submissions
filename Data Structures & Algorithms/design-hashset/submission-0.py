class MyHashSet:

    def __init__(self):
        self.array=["x"]*1000000
        

    def add(self, key: int) -> None:
        self.array[key]=key
        

    def remove(self, key: int) -> None:
        self.array[key]="x"
        

    def contains(self, key: int) -> bool:
        if self.array[key]!="x":
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)