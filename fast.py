'''
low hanging fruit would be to compare w1+w2 and w2+w1, half the search time, but i feel like we can do better than quadratic
if a trie was assembled that denoted when a full word had been assembled, for each 6 letter word we could follow it's path on the tree and see how many sub words it has, check to see if the conjugate word w6-w1 = w2 is in it's corresponding set. So, sets are still being assembled, but so is a trie.
this is now linear 6 letter words as there will be at most 5 corresponding checks for it.
'''
def import_words():
    word_list = open('words', 'r')
    word_pools = [set() for length in range(6)]
    word_trie = {}
    print(word_pools)
    for word in word_list:
        clean_word = word.lower().strip()
        if len(clean_word) < 7:
            word_pools[len(clean_word)-1].add(clean_word)
            letters = list(clean_word)
            layer = word_trie
            for letter in letters:
                if letter not in layer:
                    layer[letter] = {}
                layer = layer[letter]
            layer['end'] = True
    return word_pools, word_trie

def find_composites(groups, trie):
    length_six = groups[5]
    composites=[]
    for target in length_six:
        path = list(target)
        candidates = []
        candidate = []
        layer = trie
        for letter in path:
            candidate.append(letter)
            if 'end' in layer[letter]:
                candidates.append(''.join(candidate))
            layer = layer[letter]
        for word1 in candidates:
            length = len(word1)
            conjugate_word = target.replace(word1, '', 1)
            conju_index = len(conjugate_word)-1
            if conjugate_word in groups[conju_index]:
                composites.append((word1, conjugate_word, target))
    return composites

def display_composites(composites):
    for combo in composites:
        print("%s + %s = %s" % combo)
    return

word_sets, word_trie = import_words()
composites = find_composites(word_sets, word_trie)
display_composites(composites)
print(len(composites))
# print(word_sets[2])

