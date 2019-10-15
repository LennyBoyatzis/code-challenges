import string

alphabet = list(string.ascii_lowercase)


class TrieNode():
    def __init__(self, value='', children=None):
        self.value = value
        self.children = set()

    def add_child(self, val):
        self.children.add(val)


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        for char in word:
            print(f'what is the char {char}')


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """


if __name__ == '__main__':
    trie = Trie()
    trie.insert('peter')
