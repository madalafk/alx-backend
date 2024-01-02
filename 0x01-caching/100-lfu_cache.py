#!/usr/bin/env python3
"""
class LFUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache represents a Least Frequently Used (LFU) caching system.

    Attributes:
        usage (list): A list to keep track of the usage order of keys.
        frequency (dict): A dictionary to store the frequency of each key.
    """

    def __init__(self):
        """
        Initialize the LFUCache class by calling the parent class's init method.
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """
        Cache a key-value pair using the Least Frequently Used (LFU) strategy.

        Args:
            key: The key to cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
            lru_lfu = {k: self.usage.index(k) for k in lfu_keys}
            discard = min(lru_lfu, key=lambda k: lru_lfu[k])
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
            del self.usage[self.usage.index(discard)]
            del self.frequency[discard]

        self.frequency[key] = self.frequency.get(key, 0) + 1

        if key in self.usage:
            self.usage.remove(key)

        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value linked to a given key using the
        Least Frequently Used (LFU) strategy.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key if present, otherwise None.
        """
        if key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
