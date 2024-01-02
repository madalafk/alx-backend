#!/usr/bin/env python3
"""
defines the MRUCache class, which is a subclass of the BaseCaching class.
MRUCache implements a Most Recently Used (MRU) caching system.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class represents a Most Recently Used (MRU) caching system.

    Attributes:
        cache_data (dict): A dictionary to store key-value pairs in the cache.
        usage (list): A list to keep track of the usage order of keys.
    """

    def __init__(self):
        """
        Initialize the MRUCache class by calling the parent class's init method.
        """
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Cache a key-value pair using the Most Recently Used (MRU) strategy.

        Args:
            key: The key to cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[-1]))
                del self.cache_data[self.usage[-1]]
                del self.usage[-1]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value linked to a given key using the Most Recently Used (MRU) strategy.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key if present, otherwise None.
        """
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None

