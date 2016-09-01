class CompositeFinder():
    def __init__(self, sources=['words'], size=6):
        self.word_pools = [set() for length in range(size)]
        self.size = size
        self.build_sets(sources)

    def build_sets(self, sources):
        for path in sources:
            words = open(path, 'r')
            for word in words:
                clean_word = word.lower().strip()
                char_count = len(clean_word)
                if char_count <= self.size:
                    self.word_pools[char_count-1].add(clean_word)
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
        for split in range(1, self.size):
            candidates.append( (target[:split], target[split:]) )
        return candidates

    def check_pools(self, target, candidates):
        results = []
        for split in range( self.size-1):
            left, right = candidates[split]
            left_in = left in self.word_pools[split]
            right_in = right in self.word_pools[-(split+2)]
            if left_in and right_in:
                results.append( (left, right, target))
        return results
