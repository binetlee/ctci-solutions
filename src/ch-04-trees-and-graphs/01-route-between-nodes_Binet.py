class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # last index is the destination
        dest_index = len(graph) - 1

        # record of all paths from start to destination
        path = []

        # stack for dfs traversal
        ## this is how you create a stack, where the first entry is literally a list with one 0 in it
        ## just initializing
        dfs_stack = [(0, [0])]

        # DFS approach based on stack
        while dfs_stack:

            cur_node_index, tracking = dfs_stack.pop()

            # visit each neighbor
            for neighbor_index in graph[cur_node_index]:

                if neighbor_index == dest_index:
                    # reach destination
                    path.append(tracking + [neighbor_index])

                else:
                    # push next dfs traversal into stack
                    dfs_stack.append((neighbor_index, tracking + [neighbor_index]))

        return path


Method_  # 2: Concise DFS approach based on recursion


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # last index is the destination
        self.dest = len(graph) - 1

        # record of all paths from start to destination
        self.path = []

        # DFS traversal
        def dfs(node_index, tracking):

            # Base case:
            # Destination is reached
            if node_index == self.dest:
                self.path.append(tracking + [node_index])
                return

            # Visit each neighbor
            for neighbor_index in graph[node_index]:
                dfs(neighbor_index, tracking + [node_index])

        # start from node_#0
        dfs(0, [])

        return self.path