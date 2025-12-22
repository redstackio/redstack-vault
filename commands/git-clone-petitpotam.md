---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: git-clone-petitpotam
type: command
executor: bash
data: 'git clone https://github.com/topotam/PetitPotam'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - coercion
  - petitpotam
verified: true
validated: true
---

# git-clone-petitpotam

## Command

```bash
git clone https://github.com/topotam/PetitPotam
```

## Description

Clones the PetitPotam repository from GitHub, providing Python scripts to coerce MS-EFSRPC authentication from Windows targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Public repository, no parameters needed | No |

## Examples

### Basic Usage

```bash
git clone https://github.com/topotam/PetitPotam
cd PetitPotam
```

## Expected Output

Cloning confirmation:

Cloning into 'PetitPotam'...
remote: Enumerating objects: 20, done.
...
Unpacking objects: 100% (20/20), done.

## Related

- [[procedures/MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]
- [[tools/PetitPotam]]
