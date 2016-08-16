import time
import fast
import simple

fast_start = time.time()
for cycle in range(10):
    sets, trie = fast.import_words()
    composites = fast.find_composites(sets, trie)
fast_end = time.time()

simple_start = time.time()
for cycle in range(10):
    sets = simple.import_words()
    composites = simple.find_composites(sets)
simple_end = time.time()

print(fast_end-fast_start)
print(simple_end-simple_start)
