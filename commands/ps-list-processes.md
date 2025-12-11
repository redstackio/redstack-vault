---
id: 39915843-c375-4dad-860b-483fcccfcb3e
name: ps-list-processes
type: command
executor: bash
data: ps auxww
output: null
created_at: '2025-12-09T00:20:45.079Z'
updated_at: '2025-12-09T00:20:45.079Z'
platforms:
  - Linux
tags:
  - shell
verified: false
validated: true
submitted: true
---

# ps-list-processes

## Command

```bash
ps auxww
```

## Description

Lists all processes with details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `a` | All users | Yes |
| `u` | User-oriented | Yes |
| `x` | Processes without tty | Yes |
| `ww` | Unlimited width | Yes |

## Examples

### Basic Usage

```bash
ps auxww
```

## Expected Output

List of processes.

## Related

- [[Verify Exploitation and Execute Reverse Shell]]
