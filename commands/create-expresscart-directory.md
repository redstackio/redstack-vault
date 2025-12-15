---
id: cmd-001
data: mkdir expressCart
tags:
  - setup
  - directory
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (WSL)
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.126Z'
verified: false
validated: true
submitted: true
---
# create-expresscart-directory

## Command

```bash
mkdir expressCart
```

## Description

Creates a new directory named 'expressCart' for setting up the local express-cart project during vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| expressCart | Directory name for the project | Yes |

## Examples

### Basic Usage

```bash
mkdir expressCart
```

### Advanced Usage

```bash
mkdir -p expressCart/setup
```

## Expected Output

New directory created successfully, no output if successful.

## Related

- [[commands/change-to-expresscart-directory]]
- [[procedures/Local-Setup-of-Express-Cart-Application]]
