[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1alQ5a4a)
# hw05 – Museum Visit Planner (Shortest Path in a Graph)

## Story

A museum has many **rooms** connected by **doors**. Visitors start at the **entrance** and want to reach a chosen **goal room** (for example, a special exhibit). The museum map can be seen as a graph: rooms are nodes, doors are edges.

For safety and comfort, staff want a tool that shows **one shortest path** from the entrance to the goal room, using existing doors.

You will compute a shortest path in an **unweighted, undirected** graph.

---

## Technical Description

Write a function:

```python
def shortest_path(rooms, doors, start, goal):
    ...
```

**Parameters:**
- `rooms`: list of room names (strings)
- `doors`: list of pairs `(a, b)` where `a` and `b` are room names in `rooms`. Each pair is an undirected door between `a` and `b`
- `start`: name of the start room (string)
- `goal`: name of the goal room (string)

**Return value:**
- A list of room names representing one shortest path from `start` to `goal`, including both `start` and `goal`
- If `start == goal`, return `[start]`
- If there is no path, return `[]`

**Example:**

```python
rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]

shortest_path(rooms, doors, "Entrance", "Cafe")
# -> ["Entrance", "Hall", "Gallery", "Cafe"]
```

### Constraints

- `len(rooms)` can be from 0 to 10,000
- `len(doors)` can be from 0 to 50,000
- `start` and `goal` will be names in `rooms` if `rooms` is not empty
- Doors are undirected, and there may be duplicate door entries

### Expected Complexity

- **Time:** about O(n + m), where n is the number of rooms and m is the number of doors
- **Space:** about O(n + m) for the graph, visited set, and parent tracking
- A simple breadth-first search (BFS) is enough

---

## 8 Steps of Coding – Minimal Prompts (hw05)

Drive the full 8 Steps yourself:

1. **Steps 1–2:** Explain the task in your own words
2. **Step 3:** Decide how to represent the graph and track visited rooms
3. **Step 4–5:** Plan how to explore neighbors and reconstruct the path
4. **Step 6:** Implement the algorithm in `main.py`
5. **Step 7:** Test on small graphs where you can see all paths
6. **Step 8:** Confirm the BFS complexity (O(n + m)) and check edge cases

---

## Hints (not full solutions)

- Build an adjacency list: dictionary from room name to list of neighbors
- Use BFS (queue) starting from `start` to find the shortest path to `goal`
- Store a parent for each visited room so you can reconstruct the path at the end

---

## How to Run Tests

From the repo root:

```bash
python -m pytest -q
```

To run only hw05 tests:

```bash
python -m pytest -q hw05/tests/test_hw05.py
```

---

## FAQ

**Q1: Are doors directed?**  
No. Doors are undirected. If `("A", "B")` is in `doors`, you can go from A to B and from B to A.

**Q2: What if start == goal?**  
Return a list with only that room: `[start]`.

**Q3: What if there is no path?**  
Return an empty list `[]`.

**Q4: Can I use recursion?**  
You can, but BFS with a queue is usually clearer for shortest paths.

**Q5: Do I need to handle rooms that are not in rooms but appear in doors?**  
You may assume the input is valid: all names in `doors` appear in `rooms`.

**Q6: What Big-O do you expect?**  
We expect about O(n + m) time and O(n + m) space with a BFS solution.

**Q7: How can I debug paths?**  
Print the adjacency list and the parent mapping for small examples. Draw the graph on paper and trace the steps.