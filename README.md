# Merkle Tree Python Implementation

This repository contains a Python implementation of a Merkle Tree, a fundamental data structure in cryptography and blockchain technology. Merkle Trees are binary trees where each leaf node is the hash of a data block, and each non-leaf node is the hash of its children. The root of the tree offers a cryptographic summary of all the data contained within the tree.

## Features

- **Simplicity**: Straightforward and understandable Python code for Merkle Tree operations.
- **SHA-256 Hashing**: Utilizes the SHA-256 hash function for generating node hashes, providing cryptographic security.
- **Proof Generation**: Capability to generate proofs of data inclusion without revealing the entire tree.
- **Proof Verification**: Functionality to verify the proofs, ensuring data integrity and membership with only the Merkle root.

## Usage

### Setting Up

Ensure Python is installed on your system. This code is compatible with Python 3.x versions.

To use this implementation in your project, clone this repository.

Creating a Merkle Tree
Instantiate a Merkle Tree with your data blocks (leaves):
```python
from merkle_tree import MerkleTree

leaves = ['data1', 'data2', 'data3', 'data4']
merkle_tree = MerkleTree(leaves)
```

Getting the Merkle Root
Access the root hash of the Merkle Tree, which represents the summary of all leaves:
```python
root = merkle_tree.get_root()
print(f"Merkle Root: {root}")

```

Getting the Merkle Root
Access the root hash of the Merkle Tree, which represents the summary of all leaves:
```python
root = merkle_tree.get_root()
print(f"Merkle Root: {root}")

```

Generating and Verifying Proofs
Generate a proof for a leaf's existence in the tree:
```python
index = 1  # Index of the leaf for which you want to generate a proof
proof = merkle_tree.get_proof(index)
```

Verify the proof for a leaf:
```python
leaf = 'data2'  # The data for which the proof was generated
is_valid = merkle_tree.verify_proof(leaf, proof, root)
print(f"Proof Valid: {is_valid}")
```
