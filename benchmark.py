import time
import fast
import simple

fast_start = time.time()
sets, trie = fast.import_words()
for cycle in range(10):
    composites = fast.find_composites(sets, trie)
fast_end = time.time()

simple_start = time.time()
sets = simple.import_words()
for cycle in range(10):
    composites = simple.find_composites(sets)
simple_end = time.time()

print(fast_end-fast_start)
print(simple_end-simple_start)
'''
results:
with looading in the loop,
fast 3.01 seconds
simple 5.75 second
loading outside the loop
fast 1.26 seconds
simple 4.73 seconds
so fast took 1.8~ seconds for 10 load cycles
while simple took a little under 1, however, composite finding is close to 4 times faster with the trie method.
'''
