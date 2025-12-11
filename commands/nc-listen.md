---
data: nc -vnlkp 12345
tags:
  - shell
type: command
executor: bash
platforms:
  - Linux
id: 3833d28e-df4d-4037-b708-a898a099017a
created_at: '2025-12-11T03:48:05.990Z'
updated_at: '2025-12-11T03:48:05.990Z'
verified: false
validated: true
submitted: true
---
# nc-listen

## Command

```bash
nc -vnlkp 12345
```

## Description

Listens for incoming reverse shell connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-vnlkp 12345` | Options and port | Yes |

## Examples

### Basic Usage

```bash
nc -vnlkp 4444
```

## Expected Output

Connection received

## Related

- #nc
