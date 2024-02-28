import hashlib

def hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

class MerkleTree:
    def __init__(self, leaves):
        self.leaves = [hash(leaf) for leaf in leaves]
        self.tree = self.build_tree(self.leaves)
    
    def build_tree(self, leaves):
        tree = [leaves]
        while len(leaves) > 1:
            leaves = [hash(leaves[i] + leaves[i + 1]) for i in range(0, len(leaves) - 1, 2)]
            tree.append(leaves)
        return tree
    
    def get_root(self):
        return self.tree[-1][0] if self.tree else None

    def get_proof(self, index):
        proof = []
        for layer in self.tree[:-1]:
            is_right_node = index % 2
            sibling_index = index - 1 if is_right_node else index + 1
            if sibling_index < len(layer):
                proof.append((layer[sibling_index], is_right_node))
            index //= 2
        return proof

    def verify_proof(self, leaf, proof, root):
        leaf_hash = hash(leaf)
        for sibling_hash, is_right_node in proof:
            if is_right_node:
                leaf_hash = hash(sibling_hash + leaf_hash)
            else:
                leaf_hash = hash(leaf_hash + sibling_hash)
        return leaf_hash == root
    
    def print_tree(self):
        for level, nodes in enumerate(reversed(self.tree)):
            indent = "  " * (len(self.tree) - level - 1)  # Indentation for hierarchical structure
            print(f"{indent}Level {len(self.tree) - level - 1}: ", end="")
            for node in nodes:
                truncated_node = node[:6] + "..."  # Truncate hash for readability
                print(f"[{truncated_node}]", end=" ")
            print()  # Newline for the next level


# Example usage
leaves = ['data1', 'data2', 'data3', 'data4']
merkle_tree = MerkleTree(leaves)

merkle_tree.print_tree()

root = merkle_tree.get_root()
print(root)  # 9d5f1d8b

index = 2  # For 'data3', 0-based index
proof = merkle_tree.get_proof(index)
print(proof)  

is_valid = merkle_tree.verify_proof('data3', proof, root)
print(f"Proof Valid: {is_valid}")
