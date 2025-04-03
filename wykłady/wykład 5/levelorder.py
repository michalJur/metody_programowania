# Example - use a debugger!

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Iterative method to perform level order traversal
def level_order(root):
    if root is None:
        return []

    # Create an empty queue for level order traversal
    q = []
    res = []

    # Enqueue Root
    q.append(root)
    curr_level = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            # Add front of queue and remove it from queue
            node = q.pop(0)
            res[curr_level].append(node.data)

            # Enqueue left child
            if node.left is not None:
                q.append(node.left)

            # Enqueue right child
            if node.right is not None:
                q.append(node.right)
        curr_level += 1
    return res

if __name__ == '__main__':
    #        5
    #      /   \
    #     12    13
    #   /   \     \
    #   7    14     2
    # /  \   / \    / \
    #17  23 27  3  8  11

    root = Node(5)
    root.left = Node(12)
    root.right = Node(13)

    root.left.left = Node(7)
    root.left.right = Node(14)

    root.right.right = Node(2)

    root.left.left.left = Node(17)
    root.left.left.right = Node(23)

    root.left.right.left = Node(27)
    root.left.right.right = Node(3)

    root.right.right.left = Node(8)
    root.right.right.right = Node(11)

    # Perform level order traversal and get the result
    res = level_order(root)

    # Print the result in the required format
    for level in res:
        print('[', end='')
        print(', '.join(map(str, level)), end='')
        print('] ', end='')
