---
data: mkdir poc
tags:
  - setup
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.036Z'
id: 9dbb243b-bb6f-4160-a484-42a53af25e61
verified: false
validated: true
submitted: true
---
# mkdir-poc-directory

## Command

```bash
mkdir poc
```

## Description

Creates a new directory named 'poc' to organize the proof-of-concept files for testing the express-laravel-passport vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| poc | Directory name | Yes |

## Examples

### Basic Usage

```bash
mkdir poc
```

### Advanced Usage

```bash
mkdir -p poc/tests
```

## Expected Output

Creates directory poc; no output if successful, error if directory exists.

## Related

- [[commands/cd-poc-directory]]
