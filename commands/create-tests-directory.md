---
id: 123e4567-e89b-12d3-a456-426614174006
name: create-tests-directory
type: command
executor: bash
data: mkdir tests
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.190Z'
platforms:
  - Linux
tags:
  - setup
verified: false
validated: true
submitted: true
---

# create-tests-directory

## Command

```bash
mkdir tests
```

## Description

Creates a new directory named 'tests' for setting up a test environment in Linux shell, used prior to vulnerability exploitation to isolate activities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tests | Directory name to create | Yes |

## Examples

### Basic Usage

```bash
mkdir tests
```

### Advanced Usage

```bash
mkdir -p tests/subdir
```

## Expected Output

No output on success; directory 'tests' is created in the current working directory.

## Related

- [[Related Procedure: Setup-Test-Environment-for-meta-git-Exploitation]]
