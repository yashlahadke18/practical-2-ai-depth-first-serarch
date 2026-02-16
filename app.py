import streamlit as st

st.title("Depth First Search (DFS) Visualization")

# Tree definition
tree = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: []
}

# DFS Function
def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

            # Add children in reverse order for correct traversal
            for child in reversed(tree[node]):
                stack.append(child)

    return visited

# Select starting node
start_node = st.selectbox("Select Starting Node:", list(tree.keys()))

# Run DFS
if st.button("Run DFS"):
    result = dfs(start_node)
    st.success("DFS Traversal:")
    st.write(" ➝ ".join(map(str, result)))
