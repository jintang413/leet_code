from typing import List


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
        cur.is_word = True

    def find_pairs(self, text):
        pairs = []
        for i in range(len(text)):
            cur = self.root
            for j in range(i, len(text)):
                cur = cur.children.get(text[j], None)
                if cur:
                    if cur.is_word:
                        pairs.append([i, j])
                else:
                    break
        return pairs


def index_pairs(text: str, words: List[str]) -> List[List[int]]:
    trie = Trie()
    for word in words:
        trie.insert(word)

    pairs = trie.find_pairs(text)
    return pairs
