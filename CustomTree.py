from sortedcontainers import SortedDict


class Node:
    def __init__(self, c, n_c=0, d=0, n_d=0, d_max=0, w_i=0.0, P_c=0.0):
        self.c = c
        self.n_c = n_c
        self.N_child = SortedDict()
        self.d = d
        self.n_d = n_d
        self.d_max = d_max
        self.w_i = w_i
        self.P_c = P_c

    def calculate_P_c(self):
        if self.d_max != 0 and self.n_d != 0:
            self.P_c = (self.d / self.d_max) * (self.n_c / self.n_d) * self.w_i
        else:
            self.P_c = 0.0

class Tree:
    def __init__(self):
        self.root = Node(c=None, d=0)

    def add_node(self, parent, node):
        parent.N_child[node.c] = node
        parent.d_max = max(parent.d_max, node.d)

    def find_node(self, c, node=None):
        if node is None:
            node = self.root
        if node.c == c:
            return node
        for child in node.N_child.values():
            found = self.find_node(c, child)
            if found is not None:
                return found
        return None

    def find_LCA(self, c1, c2):
        node1 = self.find_node(c1)
        node2 = self.find_node(c2)
        if node1 is None or node2 is None:
            return None
        while node1 != node2:
            if node1.d > node2.d:
                node1 = self.find_node(node1.c)
            else:
                node2 = self.find_node(node2.c)
        return node1