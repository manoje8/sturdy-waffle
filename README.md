# Data Structures & Algorithms in Python

A structured, clean, and modern repository containing implementations of fundamental **Data Structures**, **Algorithms**, and **Classic Coding Problems** in Python 3.12+.

Designed for interview preparation, algorithmic study, and practical reference.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Implemented Modules](#implemented-modules)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
  - [Problem Solutions](#problem-solutions)
  - [Study Notes & Guides](#study-notes--guides)
- [Complexity Cheat Sheet](#complexity-cheat-sheet)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Examples](#running-examples)
- [Development & Code Quality](#development--code-quality)
- [Roadmap](#roadmap)

---

## Overview

This repository provides self-contained, clean implementations with type annotations and modern Python 3.12 idioms. It is formatted and linted using [Ruff](https://github.com/astral-sh/ruff) and configured for consistent code quality with pre-commit hooks.

---

## Repository Structure

```text
├── graph/                  # Graph data structure and graph algorithms
│   ├── graph.py            # Adjacency list Graph with BFS and DFS
│   ├── dijkstra.py         # Dijkstra's single-source shortest path
│   ├── prim.py             # Prim's Minimum Spanning Tree (MST)
│   └── floyd_warshall.py   # Floyd-Warshall All-Pairs Shortest Path
├── heaps/                  # Heap data structures and operations
│   ├── heapify.py          # Min-Heapify, Max-Heapify, and Build-Heap routines
│   ├── heapsort.py         # In-place Heap Sort
│   └── priority_queue.py   # Max-Priority Queue implementation
├── linked_list/            # Linked list variants and caching structures
│   ├── list.py             # ListNode foundation
│   ├── linked_list.py      # Singly Linked List (insert, delete, reverse, Floyd's cycle detection)
│   ├── doubly_linked_list.py # Doubly Linked List
│   ├── LRU.py              # Least Recently Used (LRU) Cache (O(1) Get/Put)
│   └── LFU.py              # Least Frequently Used (LFU) Cache skeleton
├── sorting/                # Classical sorting algorithms and documentation
│   ├── bubble_sort.py      # Bubble Sort
│   ├── selection_sort.py   # Selection Sort
│   ├── insertion_sort.py   # Insertion Sort
│   ├── merge_sort.py       # Merge Sort (Divide & Conquer)
│   ├── quick_sort.py       # Quick Sort (Lomuto partitioning)
│   ├── radix_sort.py       # Radix Sort (LSD counting sort subroutine)
│   ├── topological_sort.py # Topological Sort (DFS & Kahn's in-degree BFS)
│   └── topologicalSort_notes.md # Topological sort deep dive
├── trees/                  # Tree structures and prefix trees
│   ├── BNode.py            # Binary Tree Node
│   ├── binary_search_tree.py # BST with traversals, search, deletion, min/max, validation
│   ├── trie.py             # Trie (Prefix Tree) with search and autocomplete
│   └── trie_notes.md       # Trie design & complexity notes
├── problems/               # Classic LeetCode & interview problem solutions
│   ├── binary_search.py    # Binary Search
│   ├── group_anagrams.py   # Group Anagrams (Hash Map)
│   ├── longest_inc_subsequence.py # Longest Increasing Subsequence (DP & Patience Sorting)
│   ├── max_freq_stack.py   # Maximum Frequency Stack (FreqStack - O(1))
│   ├── median_finder.py    # Find Median from Data Stream (Two Heaps)
│   ├── merge_k_sorted_list.py # Merge k Sorted Lists (Min-Heap)
│   ├── path_sum_binary.py  # Binary Tree Root-to-Leaf Path Sum
│   └── sliding_window_median.py # Sliding Window Median (SortedList)
├── notes.md                # General algorithmic patterns, priority queues, and Regex guide
├── todo.md                 # Project roadmap and upcoming algorithms
├── pyproject.toml          # Ruff and project configuration
├── Makefile                # Convenient development commands
└── main.py                 # Central execution runner / sandbox
```

---

## Implemented Modules

### Data Structures

| Module | Description | Key Features / Operations |
|---|---|---|
| [`linked_list/linked_list.py`](linked_list/linked_list.py) | Singly Linked List | Head/Indexed Insert, Delete, Search (Iterative & Recursive), In-place Reversal, Floyd's Cycle Detection (`hasCycle`, `detectCycleStart`), Middle Node Lookup |
| [`linked_list/doubly_linked_list.py`](linked_list/doubly_linked_list.py) | Doubly Linked List | Bidirectional pointers, head insertion, list traversal |
| [`linked_list/LRU.py`](linked_list/LRU.py) | LRU Cache | $O(1)$ `get` & `put` operations using Hash Map + Doubly Linked List with sentinel head/tail nodes |
| [`trees/binary_search_tree.py`](trees/binary_search_tree.py) | Binary Search Tree | Node Insertion, Deletion (with successor replacement), Search, Min/Max, Height, BST Validation (`isBST`), Traversals (In-order, Pre-order, Post-order, Level-order BFS) |
| [`trees/trie.py`](trees/trie.py) | Prefix Tree (Trie) | Word Insertion, Search, Prefix Matching (`starts_with`), Prefix Autocomplete (`get_words_with_prefix`) |
| [`heaps/heapify.py`](heaps/heapify.py) | Binary Heaps | 0-indexed `max_heapify`, `min_heapify`, and bottom-up `build_heapify` in $O(n)$ time |
| [`heaps/priority_queue.py`](heaps/priority_queue.py) | Max-Priority Queue | `heap_maximum`, `heap_extract_max`, `heap_increase_key`, and `max_heap_insert` |
| [`graph/graph.py`](graph/graph.py) | Graph | Adjacency list representation supporting directed and undirected graphs, BFS, and DFS |

---

### Algorithms

#### Sorting Algorithms (`sorting/`)
- **Bubble Sort** ([`bubble_sort.py`](sorting/bubble_sort.py)) - Iterative adjacent swaps.
- **Selection Sort** ([`selection_sort.py`](sorting/selection_sort.py)) - Repeatedly selects the minimum element.
- **Insertion Sort** ([`insertion_sort.py`](sorting/insertion_sort.py)) - In-place incremental insertion into sorted prefix.
- **Merge Sort** ([`merge_sort.py`](sorting/merge_sort.py)) - Stable divide-and-conquer sorting.
- **Quick Sort** ([`quick_sort.py`](sorting/quick_sort.py)) - Divide-and-conquer using Lomuto partitioning.
- **Radix Sort** ([`radix_sort.py`](sorting/radix_sort.py)) - Non-comparative digit-by-digit sorting with counting sort.
- **Heap Sort** ([`heaps/heapsort.py`](heaps/heapsort.py)) - In-place comparison sort using a max-heap.
- **Topological Sort** ([`sorting/topological_sort.py`](sorting/topological_sort.py)) - DAG vertex ordering via:
  1. Depth-First Search (post-order reversal + recursion-stack cycle detection)
  2. Kahn's Algorithm (in-degree BFS queue with cycle detection)

#### Graph Algorithms (`graph/`)
- **Dijkstra's Algorithm** ([`dijkstra.py`](graph/dijkstra.py)) - Single-source shortest paths for non-negative weighted graphs using min-heap priority queue ($O((V+E) \log V)$).
- **Prim's Algorithm** ([`prim.py`](graph/prim.py)) - Minimum Spanning Tree (MST) construction using min-heap priority queue.
- **Floyd-Warshall** ([`floyd_warshall.py`](graph/floyd_warshall.py)) - All-pairs shortest path dynamic programming foundation.

---

### Problem Solutions (`problems/`)

| Problem | File | Strategy | Time Complexity | Space Complexity |
|---|---|---|---|---|
| **Binary Search** | [`binary_search.py`](problems/binary_search.py) | Iterative binary search | $O(\log n)$ | $O(1)$ |
| **Group Anagrams** | [`group_anagrams.py`](problems/group_anagrams.py) | Hash Map with sorted character keys | $O(N \cdot K \log K)$ | $O(N \cdot K)$ |
| **Longest Increasing Subsequence** | [`longest_inc_subsequence.py`](problems/longest_inc_subsequence.py) | 1. Dynamic Programming<br>2. Patience Sorting (`bisect_left`) | 1. $O(n^2)$<br>2. $O(n \log n)$ | 1. $O(n)$<br>2. $O(n)$ |
| **Max Frequency Stack** | [`max_freq_stack.py`](problems/max_freq_stack.py) | Frequency map + frequency-bucketed stacks | $O(1)$ push / pop | $O(N)$ |
| **Find Median from Data Stream** | [`median_finder.py`](problems/median_finder.py) | Dual-heap (max-heap for lower half, min-heap for upper half) | $O(\log n)$ insert, $O(1)$ median | $O(n)$ |
| **Merge k Sorted Lists** | [`merge_k_sorted_list.py`](problems/merge_k_sorted_list.py) | Min-Heap priority queue indexing active heads | $O(N \log k)$ | $O(k)$ |
| **Path Sum (Binary Tree)** | [`path_sum_binary.py`](problems/path_sum_binary.py) | Recursive DFS tree traversal | $O(n)$ | $O(h)$ |
| **Sliding Window Median** | [`sliding_window_median.py`](problems/sliding_window_median.py) | Sliding window over `SortedList` | $O(n \log k)$ | $O(k)$ |

---

### Study Notes & Guides

- **[Algorithmic Patterns & Regex Notes](notes.md)**: Common interview problem patterns (Two Pointers, Sliding Window, Backtracking, DP) and an exhaustive Python regular expressions guide.
- **[Topological Sort Notes](sorting/topologicalSort_notes.md)**: Conceptual walkthroughs, in-degree mechanics, and Kahn's algorithm step-by-step breakdown.
- **[Trie Notes](trees/trie_notes.md)**: Node structure, complexity analysis, and real-world search engine / prefix tree applications.

---

## Complexity Cheat Sheet

### Sorting Algorithms

| Algorithm | Best Time | Average Time | Worst Time | Space Complexity | Stable? |
|---|---|---|---|---|---|
| **Bubble Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Selection Sort** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No |
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes |
| **Merge Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Yes |
| **Quick Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ aux | No |
| **Heap Sort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No |
| **Radix Sort** | $O(d \cdot (n + k))$ | $O(d \cdot (n + k))$ | $O(d \cdot (n + k))$ | $O(n + k)$ | Yes |

### Data Structures Operations

| Data Structure | Access | Search | Insertion | Deletion | Space |
|---|---|---|---|---|---|
| **Singly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ (head) / $O(n)$ | $O(1)$ (head) / $O(n)$ | $O(n)$ |
| **Doubly Linked List** | $O(n)$ | $O(n)$ | $O(1)$ (head/tail) | $O(1)$ (given node) | $O(n)$ |
| **Binary Search Tree** | $O(h)$ | $O(h)$ | $O(h)$ | $O(h)$ | $O(n)$ |
| **Binary Heap** | $O(1)$ (peek) | $O(n)$ | $O(\log n)$ | $O(\log n)$ (extract) | $O(n)$ |
| **Trie** | — | $O(L)$ | $O(L)$ | $O(L)$ | $O(\Sigma \cdot N \cdot L)$ |
| **LRU Cache** | $O(1)$ (`get`) | $O(1)$ | $O(1)$ (`put`) | $O(1)$ (evict) | $O(capacity)$ |

*(where $h$ is tree height, $L$ is word length, and $\Sigma$ is alphabet size)*

---

##  Getting Started

### Prerequisites

- **Python**: Version `3.12` or higher.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/manoj-selvin/sturdy-octo-waffle.git dsa
   cd dsa
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install development dependencies:
   ```bash
   make install
   # or manually:
   pip install ruff pre-commit sortedcontainers
   ```

4. Set up pre-commit hooks (optional):
   ```bash
   pre-commit install
   ```

---

### Running Examples

You can run individual modules or the central `main.py` entrypoint:

```bash
# Run central sandbox
python3 main.py

# Run specific data structures or algorithms
python3 -m graph.dijkstra
python3 -m trees.binary_search_tree
python3 -m heaps.heapsort
python3 -m sorting.quick_sort
python3 -m problems.median_finder
```

---

## Development & Code Quality

This project uses `make` and `ruff` for code style and lint checks:

```bash
# Lint code
make lint

# Automatically format and fix issues
make format

# Run all checks
make check
```

---

## Roadmap

- [ ] **Minimum Spanning Tree**:
  - [x] Prim's Algorithm
  - [ ] Kruskal's Algorithm (Disjoint Set Union / Union-Find)
- [ ] **Shortest Path Algorithms**:
  - [x] Dijkstra's Algorithm
  - [ ] Bellman-Ford Algorithm
  - [x] Floyd-Warshall Algorithm (Complete implementation)
- [ ] **Percentile & Quantile Estimations**:
  - [ ] Forward Decay
  - [ ] t-digest
  - [ ] HdrHistogram
- [ ] **Complete Caching Structures**:
  - [x] LRU Cache
  - [ ] Complete LFU Cache implementation
- [ ] **Comprehensive Unit Test Suite** (`pytest`)
