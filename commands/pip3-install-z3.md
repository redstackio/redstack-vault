---
data: pip3 install z3-solver
tags:
  - install
  - python
type: command
output: Installation of z3-solver package
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.210Z'
id: f1f21482-ba44-4e1d-9e16-232a89b34f02
verified: false
validated: true
submitted: true
---
# pip3-install-z3

## Command

```bash
pip3 install z3-solver
```

## Description

Installs the Z3 SMT solver Python library used to reverse-engineer the LCG state from observed Math.random() outputs in the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `z3-solver` | Package name | Yes |

## Examples

### Basic Usage

```bash
pip3 install z3-solver
```

### Advanced Usage

```bash
pip3 install z3-solver --user
```

## Expected Output

Successfully installed z3-solver-X.X.X

## Related

- [[commands/node-exploit-run]]
