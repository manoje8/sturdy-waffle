Linked List
    - Insertion
    - Deletion
    - Search (Iterative/Recursive)
    - Reverse the list
    - Detect the cycle (Floyd's Algorithm)

**Applications of priority queue**

1. Task Scheduling (Operating Systems) manages tasks by priority, executing high-priority tasks first in real-time systems.
2. Dijkstra's Shortest Path Algorithm uses a priority queue to find the shortest path by selecting the nearest node.
3. Huffman Encoding (Data Compression) combines least frequent symbols using a priority queue to reduce data size.
4. Merging Multiple Sorted Lists merges sorted lists by selecting the smallest element from each list.
5. A Search Algorithm (Pathfinding) prioritizes nodes based on cost to find the shortest path in navigation or games.


### Important Patterns:

- Two pointers
- Sliding window
- Binary search
- Breadth first
- Depth First
- Backtracking
- Dynamic programming
- Priority Queue


![](assets/n_depth_explanation.png)


## Regex
It's a sequence of characters that defines a search pattern.

raw string => r""

```
good_pattern = r"\\"
```

### The Atoms - The Fundamental Particles

A regex pattern is built from atoms. These are the basic units that match a single character.

1. **Ordinary Characters**: The simplest atom. The letter `a` matches the character 'a'. The pattern `cat` matches the string 'cat'. Case-sensitive by default.

2. **The Wildcard (`.`)**: The dot is a cosmic joker. It matches _any single character_ except a newline.

    - Pattern: `c.t`

    - Matches: "cat", "c3t", "c t", "c!t"

    - Does not match: "ct"

3. **Character Classes (`[]`)**: A custom-made atom. It matches _any one character_ from a set you define.

    - `[aeiou]` matches any lowercase vowel.

    - `[a-z]` matches any lowercase letter.

    - `[a-zA-Z0-9]` matches any alphanumeric character.

    - **Negation**: Put a caret `^` at the start. `[^0-9]` matches any character that is _not_ a digit.

4. **Shorthand Character Classes**: Pre-built classes for common tasks. We use these constantly.

    - `\d` : Any digit (0-9). Equivalent to `[0-9]`.

    - `\D` : Any non-digit. Equivalent to `[^0-9]`.

    - `\w` : Any "word" character (a-z, A-Z, 0-9, and the underscore `_`). Equivalent to `[a-zA-Z0-9_]`.

    - `\W` : Any non-word character.

    - `\s` : Any whitespace character (space, tab, newline, carriage return).

    - `\S` : Any non-whitespace character.


### The Quantifiers - The Rule of Repetition

An atom defines _what_ to match. A quantifier, placed immediately after, defines _how many_.

- `?` : The atom is optional. Matches 0 or 1 times. Think of it as "the atom may appear, once, or not at all." `colou?r` matches "color" and "colour".

- `*` : Matches 0 or more times. The atom is optional and can repeat. `oh*` matches "o", "oh", "ohh", "ohhh", etc.

- `+` : Matches 1 or more times. The atom _must_ appear at least once. `oh+` matches "oh", "ohh", but not "o".

- `{m,n}` : The precise quantifier. Matches from `m` to `n` repetitions.

    - `a{3}` : Exactly three 'a's. "aaa".

    - `a{2,4}` : Two, three, or four 'a's.

    - `a{2,}` : Two or more 'a's.

#### The Convenience Functions (for quick, one-off operations)

- **`re.search(pattern, string)`**: Scans the entire string and returns a **Match object** for the _first_ successful match. If no match, returns `None`.

- **`re.match(pattern, string)`**: Determines if the pattern matches _at the beginning of the string_. Returns a Match object or `None`. This is a common source of bugs; do not confuse it with `search`.

- **`re.findall(pattern, string)`**: Returns a list of all non-overlapping matches as strings.

- **`re.sub(pattern, replacement, string)`**: The Swiss Army knife. Finds all matches and replaces them. Returns a new string.
