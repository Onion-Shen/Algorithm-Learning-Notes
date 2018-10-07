from typing import Any, List


class Bucket(object):
    def __init__(self, key: Any, value: Any):
        self.key: Any = key
        self.value: Any = value


class HashTable_linkedList(object):
    def __init__(self):
        self.count: int = 0
        self.slots: int = 10
        self.buckets: List[List[Bucket]] = [None] * self.slots

    def hash(self, key) -> int:
        return int(hash(key) % self.slots)

    def resize(self):
        result = self.count / self.slots
        if result < 0.8:
            return

        copyItems = []
        for linkedList in self.buckets:
            if not linkedList:
                continue

            for bucket in linkedList:
                copyItems.append(bucket)

        self.slots = int(self.slots * 5 / 4)
        self.count = 0

        self.buckets.clear()
        self.buckets = [None] * self.slots

        for bucket in copyItems:
            self.insert(bucket.key, bucket.value)

    def insert(self, key: Any, value: Any):
        index = self.hash(key)
        if index < 0 or index > self.slots:
            return

        linkedList = self.buckets[index]
        if linkedList is None:
            linkedList = []
            self.buckets[index] = linkedList

        for bucket in linkedList:
            if bucket.key == key:
                bucket.value = value
                break
        else:
            linkedList.append(Bucket(key, value))
            self.count += 1

        self.resize()

    def __setitem__(self, key: Any, value: Any):
        self.insert(key, value)

    def search(self, key: Any) -> Any:
        index = self.hash(key)
        if index < 0 or index > self.slots:
            return None

        linkedList = self.buckets[index]
        for bucket in linkedList:
            if bucket.key == key:
                return bucket.value

        return None

    def __getitem__(self, key: Any) -> Any:
        return self.search(key)

    def delete(self, key: Any):
        index = self.hash(key)
        if index < 0 or index > self.slots:
            return

        linkedList = self.buckets[index]
        if not linkedList:
            return

        j = -1
        for i in range(0, len(linkedList)):
            bucket = linkedList[i]
            if bucket.key == key:
                j = i
                break

        if j == -1:
            return

        linkedList.pop(j)
        self.count -= 1
