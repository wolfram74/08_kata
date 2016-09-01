def import_words():
    word_list = open('words', 'r')
    word_pools = [set() for length in range(6)]
    # print(word_pools)
    for word in word_list:
        clean_word = word.lower().strip()
        if len(clean_word) < 7:
            word_pools[len(clean_word)-1].add(clean_word)
    return word_pools

def find_composites(groups):
    length_six = groups[5]
    composites=[]
    for length in range(5):
        part1 = groups[length]
        part2 = groups[4-length]
        for word1 in part1:
            for word2 in part2:
                if word1+word2 in length_six:
                    composites.append((word1, word2, word1+word2))
    return composites

def display_composites(composites):
    for combo in composites:
        print("%s + %s = %s" % combo)
    return

# word_sets = import_words()
# composites = find_composites(word_sets)
# display_composites(composites)
# print(len(composites))

26+ 139+ 1294+ 4994+ 9972+ 17462
