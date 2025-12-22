---
id: f13a10ef-3aaa-4576-8f02-a59c8d6dbdeb
name: cd-to-tickey-directory
type: command
executor: bash
data: cd tickey/tickey
output: null
created_at: '2023-04-06T03:56:08.565579+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - navigation
  - setup
verified: true
validated: true
---

# Cd to Tickey Directory

## Command

```bash
cd tickey/tickey
```

## Description

Changes the current working directory to the Tickey source subdirectory, preparing for the build process after cloning the repository.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tickey/tickey | Path to the Tickey source directory | Yes |

## Examples

### Basic Usage

```bash
cd tickey/tickey
```

### Absolute Path Usage

```bash
cd /path/to/cloned/tickey/tickey
```

## Expected Output

No output; the shell prompt updates to reflect the new directory (verifiable with `pwd`).

## Related

- [[procedures/extract-ccache-tickets-from-linux-keyring-with-tickey]]
- [[tools/tickey]]
