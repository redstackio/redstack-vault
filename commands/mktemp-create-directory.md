---
id: fa509aa2-461b-45b1-8f08-485db4ae66a6
name: mktemp-create-directory
type: command
executor: bash
data: EXPLOIT_DIR=$(mktemp -d)
output: Assigns temp path to variable
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.005Z'
platforms:
  - Linux
tags:
  - temp-dir
  - setup
verified: false
validated: true
submitted: true
---

# mktemp-create-directory

## Command

```bash
EXPLOIT_DIR=$(mktemp -d)
```

## Description

Creates a unique temporary directory and assigns its path to the EXPLOIT_DIR variable for use in exploit setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | Create directory instead of file | Yes |
| $( ) | Captures output to variable | Yes |

## Examples

### Basic Usage

```bash
EXPLOIT_DIR=$(mktemp -d)
```

### Advanced Usage

```bash
EXPLOIT_DIR=$(mktemp -d -p /custom/tmp)
```

## Expected Output

No direct output; $EXPLOIT_DIR holds path like /tmp/tmp.ABC123.

## Related

- [[commands/ln-create-symlink]]
- [[procedures/Setup-Exploit-Directory-and-Symbolic-Link]]
