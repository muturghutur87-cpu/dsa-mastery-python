from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache implementation using OrderedDict.
    Maintains O(1) time complexity for both 'get' and 'put' operations.
    """
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

def run_tests():
    """
    Professional test suite to verify LRU logic and edge cases.
    """
    print("Running LRU Cache stress tests...")
    cache = LRUCache(2)

    # Test 1: Basic Put/Get
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1, "Test 1 Failed"

    # Test 2: Verify Eviction (Least recently used '2' should be removed)
    cache.put(3, 3) # This should evict key 2
    assert cache.get(2) == -1, "Test 2 Failed: Key 2 should have been evicted"
    
    # Test 3: Verify Order Update on Get
    cache.get(1)    # 1 is now most recent
    cache.put(4, 4) # This should evict key 3, NOT key 1
    assert cache.get(3) == -1, "Test 3 Failed: Key 3 should have been evicted"
    assert cache.get(1) == 1, "Test 3 Failed: Key 1 should still exist"

    print("All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
