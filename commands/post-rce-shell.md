---
data: COMMAND
tags:
  - post-exploit
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.195Z'
id: 6c0e454c-4e32-4cf7-8dac-c23018deac56
verified: false
validated: true
submitted: true
---
# post-rce-shell

## Command

```bash
COMMAND
```

## Description

Generic shell command executed post-RCE for file mods, recon, or exfil.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `COMMAND` | Specific shell cmd like echo or nmap | Yes |

## Examples

### Basic Usage

```bash
echo "Hacked" > index.html
```

### Advanced Usage

```bash
nmap -sP 192.168.1.0/24
```

## Expected Output

Command results, e.g., file written or hosts listed.

## Related

- [[commands/curl-traversal]]
