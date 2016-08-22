class CompositeFinder():
    def __init__(self, sources=['words'], size=6):
        self.word_pools = [set() for length in range(size)]
        self.size = size
        self.word_trie = {}
        self.build_sets(sources)
        self.build_trie()

    def build_sets(self, sources):
        for path in sources:
            words = open(path, 'r')
            for word in words:
                clean_word = word.lower().strip()
                char_count = len(clean_word)
                if char_count <= self.size:
                    self.word_pools[char_count-1].add(clean_word)
        return

    def build_trie(self):
        for pool in self.word_pools:
            for word in pool:
                layer = self.word_trie
                for letter in list(word):
                    if letter not in layer:
                        layer[letter] = {}
                    layer = layer[letter]
                layer['end'] = True
        return

    def find_composites(self):
        targets = self.word_pools[self.size-1]
        composites = []
        for target in targets:
            candidates = self.find_candidates(target)
            subset = self.check_pools(target, candidates)
            for composite in subset:
                composites.append(composite)
        return composites

    def find_candidates(self, target):
        candidates = []
        visited = []
        layer = self.word_trie
        for letter in list(target):
            visited.append(letter)
            if 'end' in layer[letter]:
                candidates.append(''.join(visited))
            layer = layer[letter]
        return candidates

    def check_pools(self, target, candidates):
        results = []
        for word1 in candidates:
            conjugate_word = target.replace(word1, '', 1)
            conju_index = len(conjugate_word)-1
            if conjugate_word in self.word_pools[conju_index]:
                results.append((word1, conjugate_word, target))
        return results
