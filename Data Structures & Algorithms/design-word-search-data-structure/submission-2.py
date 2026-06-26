class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            c = word[i]
            if c == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                idx = ord(c) - ord('a')
                if not node.children[idx]:
                    return False
                return dfs(node.children[idx], i + 1)
        return dfs(self.root, 0)
