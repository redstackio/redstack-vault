---
id: 123e4567-e89b-12d3-a456-426614174007
name: navigate-to-tests
type: command
executor: bash
data: cd tests
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.188Z'
platforms:
  - Linux
tags:
  - navigation
verified: false
validated: true
submitted: true
---

# navigate-to-tests

## Command

```bash
cd tests
```

## Description

Changes the current working directory to 'tests', allowing subsequent file operations within the test environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| tests | Target directory path | Yes |

## Examples

### Basic Usage

```bash
cd tests
```

### Advanced Usage

```bash
cd /full/path/to/tests
```

## Expected Output

Shell prompt updates to reflect the new directory, e.g., '/path/to/tests $'.

## Related

- [[Related Procedure: Setup-Test-Environment-for-meta-git-Exploitation]]
