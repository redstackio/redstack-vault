---
data: ls
tags:
  - inspection
type: command
output: app  config  test.html  README.md ...
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.364Z'
id: 78ad4e32-b966-4839-949a-c370d5eb3f2f
verified: false
validated: true
submitted: true
---
# ls-root-dir

## Command

```bash
ls
```

## Description

Lists root directory to verify traversal write.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Current dir | No |

## Examples

### Basic Usage

```bash
ls
```

## Expected Output

test.html visible.

## Related

- [[commands/curl-traversal-test]]
