---
data: uname -a > /tmp/alexb-says-hi
tags:
  - rce
  - system-info
type: command
output: System uname string written to file
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.185Z'
id: 169129c3-2b06-4102-bfa0-71fbfdd505a6
verified: false
validated: true
submitted: true
---
# uname-payload-write

## Command

```bash
uname -a > /tmp/alexb-says-hi
```

## Description

Executes via RCE payload to write full system uname information to a file in /tmp for verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Show all info (kernel, hostname, etc.) | Yes |
| `> /tmp/alexb-says-hi` | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
uname -a > /tmp/alexb-says-hi
```

## Expected Output

No stdout; file /tmp/alexb-says-hi contains 'Linux [details]'.

## Related

- [[commands/cat-tmp-alexb-says-hi]]
- [[procedures/Verify-RCE-Execution-in-Tmp-Directory]]
