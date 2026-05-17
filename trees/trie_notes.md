## Trie
A Trie (pronounced "try") is a tree-like data structure used to store and retrieve strings efficiently. 
Each node represents a character, and paths from root to leaf represent complete words.

        root
       /    \
      c      d
      |      |
      a      o
     / \    / \
    t   r  g   (end)
(end)(end)|(end)

## Time Complexities:

Insert: O(m) where m is word length
Search: O(m)
Delete: O(m)
Prefix Search: O(m)

### Space Complexity:

O(ALPHABET_SIZE * N * m) where N is number of words and m is average length

## Common Applications:

* Autocomplete/Suggestions - Find all words with a prefix
* Spell Checker - Check if a word exists
* IP Routing - Longest prefix matching
* Dictionary Implementation - Efficient word storage and retrieval
* Word Games - Like Boggle or Scrabble

## Advantages:

* Fast prefix-based operations
* Efficient for dictionary-like data
* No hash collisions like in hash tables

## Disadvantages:

* High memory usage for large alphabets
* Not cache-friendly due to pointer chasing


The Trie structure is particularly powerful when you need prefix-based operations,
making it ideal for autocomplete systems and dictionary implementations!