##https://leetcode.com/problems/all-paths-from-source-to-target/

##Takeaway, if you don't UNDERSTAND THE PROBLEM AT ALL, don't bother looking at the solution
##What this means [[1,2], [3], [3], []]
## as a DIRECTED GRAPH node 0 is directed to nodes 1,2
## node 1 is only directed to node 3 (even though it still ties back to node 0)
## node 2 is only directed to node 3 (even though it still ties back to node 0)
## node 3 has no directions (even though it still has connections to 1,2)

##Takeaway, it seems the base case requires a little more depth into the initial case
    ##recursion derives the state from the beginning
    ##iteration requires a little more work
Method_  # 1: Concise DFS approach based on recursion



class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph) - 1

        paths = []
        ##recurse function to look for neighbors
        ##YMU by having two of the same name in the vars
        def dfs(new_index, cur_path):
            ##params: new index, paths
            ##base case: reach destination
            ##approve the current path + the new node as a list
            if new_index == dest:
                paths.append(cur_path + [new_index])
            ##do neighbors
            ##call recursively on every element to find next potential neighbor
            ##YMU by passing the new_index into the recursive function as the new_index, going nowhere
            else:
                for ele in graph[new_index]:
                    dfs(ele, cur_path + [new_index])


        ##Call recursive function, which should be the start BASE CASE
        ##YMU by putting paths, which would just be an infinite loop
        dfs(0, [])

        return paths

Method_  # 2: Implement same problem but instead of recursion, do it iteratively with DFS in a stack
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ##To implement a DFS recursive method iteratively using a stack
        ##for stack create a while-for
        ##while stack is not empty
        ##pop item off stack before for
        ##within for you'll make changes, and append to the stack when necessary

        ##start with your elements that can be derived from the problem information
        dest = len(graph) - 1

        paths = []

        ##when going iteratively, you have to instantiate your initial stack
        ##YMU by trying to create a function for the iterative approach, THIS ISNT RECURSION
        ##initial stack should contain the literal base case starting point
            ##which in this case is an array with the starting point of [0]
        ## when creating a stack for iteration, think about what the initial case should be
        ## that's what the stack should be instantiated as, you're going to decouple as necessary after

        stack = [(0, [0])]

        while stack:
            ##YMU by popping just the one element,
            ## if your stack is more complicated, you can decouple at this stage too
            new_index,cur_path = stack.pop()

            ##for loop
            ##YMU by not knowing how to construct the for loop
            ##YMU by not understanding which index to pass next, understand and visualize better with practice
            ##Keep in mind that the next goal will be to read the index contents for next step
            for neigh_index in graph[new_index]:
                ##if next index is the destination
                if neigh_index == dest:
                    paths.append(cur_path+[neigh_index])
                else:
                    ##add back on to the stack
                    stack.append((neigh_index,cur_path+[neigh_index]))


        ##ret it
        return paths



