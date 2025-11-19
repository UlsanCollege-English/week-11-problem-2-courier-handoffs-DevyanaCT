from collections import deque
from typing import Dict, List, Optional, Any

def bfs_path(graph: Dict[Any, List[Any]], s: Any, t: Any) -> Optional[List[Any]]:
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    - If s == t and s in graph: return [s]
    - If s or t not in graph: return None
    - If no path: return None
    """

    # Check presence
    if s not in graph or t not in graph:
        return None

    # Special case
    if s == t:
        return [s]

    queue = deque([s])
    visited = {s}
    parent = {s: None}

    # BFS
    while queue:
        node = queue.popleft()
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                if nbr == t:
                    queue.clear()
                    break
                queue.append(nbr)

    # If t was never reached
    if t not in parent:
        return None

    # Reconstruct path
    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    return list(reversed(path))
