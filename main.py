


def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    rooms: list of room name strings.
    doors: list of (a, b) pairs, each pair is an undirected door between rooms a and b.
    start: start room name.
    goal: goal room name.

    Return:
      - list of room names from start to goal (inclusive) for one shortest path,
      - [start] if start == goal,
      - [] if no path exists.
    """

    # Validate that start and goal are in the set of known rooms.
    room_set = set(rooms)
    if start not in room_set or goal not in room_set:
        # If either endpoint is unknown, there is no path.
        return []

    # Trivial case: start == goal
    if start == goal:
        return [start]

    # Build adjacency list for an undirected graph. Include isolated rooms.
    adj = {r: [] for r in rooms}
    for a, b in doors:
        # Only add edges between known rooms (ignore doors referring to unknown rooms)
        if a in adj and b in adj:
            adj[a].append(b)
            adj[b].append(a)

    # BFS
    from collections import deque

    q = deque([start])
    parent = {start: None}

    found = False
    while q:
        cur = q.popleft()
        if cur == goal:
            found = True
            break
        for nbr in adj.get(cur, []):
            if nbr not in parent:
                parent[nbr] = cur
                q.append(nbr)

    if not found:
        return []

    # Reconstruct path from goal back to start
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent.get(node)
    path.reverse()
    return path


if __name__ == "__main__":
    # Optional manual test
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
