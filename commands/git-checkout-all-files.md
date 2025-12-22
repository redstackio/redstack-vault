---
type: command
executor: bash
data: git checkout -- .
output: null
created_at: '2023-04-06T03:56:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - git
  - checkout
  - reconstruction
verified: true
validated: true
---

# git-checkout-all-files

## Command

```bash
git checkout -- .
```

## Description

This command checks out all files from the current Git branch in the dumped repository, materializing the source code structure locally after using gitdumper. It ensures all tracked files are visible and ready for analysis or exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -- . | Checkout all files in the current directory and subdirectories | Yes |

## Examples

### Basic Usage

```bash
git checkout -- .
```

### In Specific Branch

```bash
git checkout main -- .
```

## Expected Output

Updated 50 files
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

Or, if no changes: "Already up to date."

## Related

- [[Related Procedure|procedures/Exploit-Insecure-Git-Repository-with-GitTools]]
