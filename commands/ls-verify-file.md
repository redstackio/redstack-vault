---
data: ls me
tags:
  - ls
  - verification
type: command
executor: bash
platforms:
  - Linux
id: 971000a3-ecbc-41d4-95fb-8e31a135af4c
created_at: '2025-12-13T09:01:16.856Z'
updated_at: '2025-12-13T09:01:16.856Z'
verified: false
validated: true
submitted: true
---
# ls-verify-file

## Command

```bash
ls me
```

## Description

Lists information about the file 'me' to confirm RCE by checking if it was created.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `me` | File to list | Yes |

## Examples

### Basic Usage

```bash
ls me
```

## Expected Output

"me" (if file exists).

## Related

- [[procedures/Verify-RCE-Exploitation]]
