---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: git-clone-iphelix-pack
type: command
executor: bash
data: 'git clone https://github.com/iphelix/pack'
output: null
created_at: '2023-04-06T03:56:04.096865+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - setup
  - mask-generation
verified: true
validated: true
---

# git-clone-iphelix-pack

## Command

```bash
git clone https://github.com/iphelix/pack
```

## Description

Clones the iphelix/pack repository, which contains Python scripts (statsgen.py and maskgen.py) for generating custom masks for Hashcat based on potfile analysis. Use this to set up the tools for offline password pattern optimization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/iphelix/pack | Repository URL for the mask generation pack | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/iphelix/pack
```

### With Specific Directory

```bash
git clone https://github.com/iphelix/pack mask_tools
```

## Expected Output

Cloning into 'pack'...
remote: Enumerating objects: X, done.
remote: Total X (delta Y), reused Z (delta W), pack-reused 0
Receiving objects: 100% (X/Y), done.

## Related

- [[procedures/Crack-NTLM-Hashes-with-Hashcat]]
- [[tools/Hashcat]]
