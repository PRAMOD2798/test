import csv
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.adj[node])
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_util(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj[node]:
                    dfs_util(neighbor)

        dfs_util(start)
        return result

    def to_vis_format(self):
        nodes = [{"id": node, "label": node} for node in self.adj.keys()]
        edges = []
        seen = set()
        for node, neighbors in self.adj.items():
            for neighbor in neighbors:
                if (neighbor, node) not in seen:
                    edges.append({"from": node, "to": neighbor})
                    seen.add((node, neighbor))
        return {"nodes": nodes, "edges": edges}

    def load_from_csv(self, path):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.add_edge(row['influencer'], row['connection'])
