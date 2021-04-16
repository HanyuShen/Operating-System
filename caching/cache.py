from memory import Memory

# Your implementations of the classes below should not include any additional print statements. 


class CyclicCache(Memory):
    def name(self):
        return "Cyclic"

    # Edit the code below to provide an implementation of a cache that
    # uses a cyclic caching strategy with a cache size of 4. You can
    # use additional methods and variables as you see fit as long as you
    # provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()
        self.cache = [(None,None),(None,None),(None,None),(None,None)]

    def lookup(self,address):
        for cache_address in self.cache:
            if address == cache_address:
                self.hit_count -= 1
                return super().lookup(address)
    
        if len(self.cache) > 3:
            del self.cache[0]
            self.cache.append(address)
        else:
            self.cache.append(address)    

        return super().lookup(address)



class LRUCache(Memory):
    def name(self):
        return "LRU"

    # Edit the code below to provide an implementation of a cache that
    # uses a least recently used caching strategy with a cache size of
    # 4. You can use additional methods and variables as you see fit as
    # long as you provide a suitable overridding of the lookup method.

    def __init__(self):
        super().__init__()
        self.cache = [(None, None), (None, None), (None, None), (None, None)]

    def lookup(self, address):
        addresses = [x[0] for x in self.cache]
        cacheData = [x[1] for x in self.cache]
        if address not in addresses:
            self.cache = self.cache[1:]
            self.cache.append((address, super().lookup(address)))
            addresses = [x[0] for x in self.cache]
            cacheData = [x[1] for x in self.cache]
            return cacheData[addresses.index(address)]
        else:
            index = addresses.index(address)
            self.cache = self.cache[0:index] + self.cache[index+1:]
            self.cache.append((address, cacheData[index]))
            return cacheData[addresses.index(address)]+"(not hit)"


     


