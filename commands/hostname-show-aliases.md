---
id: cmd-uuid-3
data: hostname -a
tags:
  - recon
  - host-enum
type: command
output: web-09-sv-gprd
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.920Z'
verified: false
validated: true
submitted: true
---
# hostname-show-aliases

## Command

```bash
hostname -a
```

## Description

Shows all FQDN aliases of the host, used in reverse shell to identify the GitLab server during RCE verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -a | Show all aliases | Yes |

## Examples

### Basic Usage

```bash
hostname -a
```

### Advanced Usage

```bash
hostname -f
```

## Expected Output

web-09-sv-gprd (or similar server hostname)

## Related

- [[commands/ps-list-processes]]
- [[procedures/Verify-RCE-Impact-with-File-Write-or-Reverse-Shell]]
