---
data: git rev-parse HEAD
tags:
  - git
  - verification
type: command
executor: bash
platforms:
  - Linux
id: 1f1d4ffa-d7f6-4308-b366-e8bc1031c034
created_at: '2025-12-13T09:01:16.874Z'
updated_at: '2025-12-13T09:01:16.874Z'
verified: false
validated: true
submitted: true
---
# git-rev-parse-head

## Command

```bash
git rev-parse HEAD
```

## Description

Retrieves the SHA-1 hash of the current commit to verify the code version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `HEAD` | Reference to the current commit | Yes |

## Examples

### Basic Usage

```bash
git rev-parse HEAD
```

## Expected Output

A commit hash like 0fb6993f48bb01a960316027675f3f496baa2088.

## Related

- [[procedures/Verify-Git-Commit-Hash]]
- [[tools/git]]
