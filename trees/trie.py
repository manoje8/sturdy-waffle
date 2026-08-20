class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        temp = self.root

        for char in word:
            if char not in temp.children:
                temp.children[char] = TreeNode()

            temp = temp.children[char]

        temp.is_end_of_word = True

    def search(self, word) -> bool:
        temp = self.root

        for char in word:
            if char not in temp.children:
                return False

            temp = temp.children[char]

        return temp.is_end_of_word

    def starts_with(self, prefix):
        # Start from root
        current = self.root

        # Traverse through each character
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        # If we traversed all characters, prefix exists
        return True

    def get_words_with_prefix(self, prefix):
        temp = self.root
        result = []
        for char in prefix:
            if char not in temp.children:
                return temp

            temp = temp.children[char]

        self._dfs(temp, prefix, result)

        return result

    def _dfs(self, node, current_word, result):
        if node.is_end_of_word:
            result.append(current_word)

        for char, _node in node.children.items():
            self._dfs(node, current_word + char, result)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("cat")
    trie.insert("dog")
    trie.insert("dollar")
    trie.insert("donkey")
    print(trie.search("dog"))
    print(trie.get_words_with_prefix("do"))
