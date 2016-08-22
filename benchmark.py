import time
import fast
import modular
import simple

fast_start = time.time()
sets, trie = fast.import_words()
print([len(group) for group in sets])
# for cycle in range(10):
#     composites = fast.find_composites(sets, trie)
# fast_end = time.time()

simple_start = time.time()
sets = simple.import_words()
# for cycle in range(10):
#     composites = simple.find_composites(sets)
# simple_end = time.time()

# print(fast_end-fast_start)
# print(simple_end-simple_start)
fastComp = fast.find_composites(sets, trie)
slowComp = simple.find_composites(sets)
module = modular.CompositeFinder()
print(type( module))
modComp = module.find_composites()
print([len(slowComp), len(fastComp), len(modComp)])
find_size_9 = modular.CompositeFinder(size=15)
print([len(group) for group in find_size_9.word_pools])
print(len(find_size_9.find_composites()))
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
