---
id: b3f4a14d-d2a9-4c68-89ae-8dda1339daa9
name: hostname-display-alias
type: command
executor: bash
data: hostname -a
output: null
created_at: '2025-12-09T00:20:45.076Z'
updated_at: '2025-12-09T00:20:45.076Z'
platforms:
  - Linux
tags:
  - shell
verified: false
validated: true
submitted: true
---

# hostname-display-alias

## Command

```bash
hostname -a
```

## Description

Displays hostname aliases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Alias names | Yes |

## Examples

### Basic Usage

```bash
hostname -a
```

## Expected Output

web-30-sv-gprd

## Related

- [[Verify Exploitation and Execute Reverse Shell]]
