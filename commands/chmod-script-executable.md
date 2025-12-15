---
id: 8519f4cf-a2f4-40f0-956f-38de14a8581d
name: chmod-script-executable
type: command
executor: bash
data: chmod +x data-fetcher.sh
output: No output
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:16.959Z'
platforms:
  - Linux
tags:
  - permissions
  - script
verified: false
validated: true
submitted: true
---

# chmod-script-executable

## Command

```bash
chmod +x data-fetcher.sh
```

## Description

Adds execute permission to the exploit script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| +x | Add execute bit | Yes |
| data-fetcher.sh | Script file | Yes |

## Examples

### Basic Usage

```bash
chmod +x script.sh
```

## Expected Output

None; permissions updated.

## Related

- [[commands/run-exploit-script]]
- [[procedures/Execute-Full-Exploit-Script]]
