#!/usr/bin/python3
"""
defines the LFUCache class, which is a subclass of the BaseCaching class.
LFUCache implements a Least Frequently Used (LFU) caching system.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class represents a Least Frequently Used (LFU) caching system.

    Attributes:
        cache_data (OrderedDict): An ordered dictionary to store
        key-value pairs in the cache.
        mru (str): Most Recently Used key in the cache.
    """

    def __init__(self):
        """
        Initialize the LFUCache class by calling the parent class's init method.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.mru = ""

    def put(self, key, item):
        """
        Add an item to the LFUCache.

        Args:
            key: The key to cache.
            item: The value associated with the key.

        Returns:
            None
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.mru = key
                else:
                    # Discard the most recently used item
                    discarded = self.mru
                    del self.cache_data[discarded]
                    print("DISCARD: {}".format(discarded))
                    self.cache_data[key] = item
                    self.mru = key
            else:
                self.cache_data[key] = item
                self.mru = key

    def get(self, key):
        """
        Get an item from the LFUCache.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key if present, otherwise None.
        """
        if key in self.cache_data:
            self.mru = key
            return self.cache_data[key]
