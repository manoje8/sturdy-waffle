A **topological ordering** of a directed graph is a linear ordering of its vertices such that for every directed edge `u → v`, `u` comes before `v` in the ordering.

**Key constraint:** The graph must be a **DAG** (Directed Acyclic Graph). If there's any cycle, no topological order exists — you can't have `A before B` and `B before A` simultaneously.

**Real-world analogy:** Think of university course prerequisites:

- To take Calculus II, you must first pass Calculus I.

- Topological sort gives you a valid sequence to take all courses without violating prerequisites.


---

## Two Approaches

you should know both:

|Method|Idea|Use case|
|---|---|---|
|**DFS + Stack**|Post-order DFS, push nodes after exploring children|Elegant, natural for recursion|
|**Kahn's Algorithm (BFS)**|Iteratively remove nodes with in-degree 0|Good for scheduling, parallelism detection|

---

## 3. Our Example Graph

Let's take a practical problem: **build system dependencies**.

```
Nodes: A, B, C, D, E, F
Edges (u → v means "u must be built before v"):
  A → C
  A → D
  B → D
  B → E
  C → F
  D → F
  E → F
```

Draw it mentally:

```
A ──→ C ──┐
│         │
└──→ D ───┼──→ F
     ↑    │
B ───┤    │
│         │
└──→ E ───┘
```

Visually, F depends on C, D, E. D depends on A, B. Etc.

---

## Method 1: DFS + Stack

### The mental model

- Run DFS from unvisited nodes.

- When you're done exploring all descendants of a node, push it onto a stack.

- After DFS completes, the stack's reverse gives the topological order.

- Why? The deepest dependency finishes first; it goes to the bottom of the stack.


### Step-by-step on our graph

**State tracking:**

- `visited` set — nodes fully processed

- `rec_stack` set — nodes currently in recursion (for cycle detection)

- `order` stack — result


**Execution:**


```
Start DFS from A (unvisited):
  Visit A (mark visited, add to rec_stack)
  Explore A→C:
    Visit C
    Explore C→F:
      Visit F
      F has no outgoing unvisited neighbors
      F is done → push F to stack, remove from rec_stack
    C done → push C
  Explore A→D:
    Visit D
    Explore D→F: already visited (fully processed), skip
    D done → push D
  A done → push A
Start DFS from B (unvisited):
  Visit B
  Explore B→D: already visited, skip
  Explore B→E:
    Visit E
    Explore E→F: already visited, skip
    E done → push E
  B done → push B
  ```

**Stack state (bottom to top):** `[F, C, D, A, E, B]`

**Topological order (reverse stack):** `B, E, A, D, C, F`

Verify:

- B before D? ✓
- B before E? ✓
- A before C? ✓
- A before D? ✓
- C before F? ✓
- D before F? ✓
- E before F? ✓

## Method 2: Kahn's Algorithm (BFS)

### The mental model

- Compute **in-degree** (number of incoming edges) for each node.

- Start with all nodes that have in-degree 0 (no dependencies).

- Remove a node, append to result, decrease in-degree of its neighbors.

- If a neighbor's in-degree becomes 0, add to queue.

- At the end, if result length ≠ number of nodes → cycle exists.


### Step-by-step on our graph

**Initial in-degrees:**

```
A: 0    (no incoming)
B: 0
C: 1    (from A)
D: 2    (from A, B)
E: 1    (from B)
F: 3    (from C, D, E)
```

**Execution:**

```
Queue: [A, B]           → start with in-degree 0 nodes
Result: []

Pop A → Result: [A]
  Reduce C's in-degree: 1→0 → add C to queue
  Reduce D's in-degree: 2→1

Pop B → Result: [A, B]
  Reduce D's in-degree: 1→0 → add D to queue
  Reduce E's in-degree: 1→0 → add E to queue

Pop C → Result: [A, B, C]
  Reduce F's in-degree: 3→2

Pop D → Result: [A, B, C, D]
  Reduce F's in-degree: 2→1

Pop E → Result: [A, B, C, D, E]
  Reduce F's in-degree: 1→0 → add F to queue

Pop F → Result: [A, B, C, D, E, F]
```

**Result:** `A, B, C, D, E, F`

This is different from the DFS result, but **equally valid** — there are often multiple valid topological orders.


## When to Use Which

|Scenario|Choose|Reason|
|---|---|---|
|Need one valid order|DFS|Simpler recursive logic|
|Need lexicographically smallest order|Kahn's + priority queue|Easy to tweak queue to min-heap|
|Need to detect parallelism layers|Kahn's|Each BFS level = parallel tasks|
|Deep graphs (risk recursion limit)|Kahn's|Iterative, no stack overflow|
|Cycle detection required|Either|Both detect cycles naturally|

---

## 7. Common Pitfalls & Tips

1. **Cycle detection** — Always include it. In interviews, missing it is a red flag.
2. **Disconnected graphs** — Always loop over all vertices to start DFS/collect in-degree 0 nodes.
3. **Multiple valid orders** — Topological sort is not unique. Don't assume one "correct" answer.
4. **Large graphs** — Prefer Kahn's with iteration to avoid recursion depth issues.
