---
id: cmd-uuid-1
data: echo "127.0.0.1 a.com" | sudo tee -a /etc/hosts
tags:
  - dns
  - hosts
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.605Z'
verified: false
validated: true
submitted: true
---
# add-hosts-entry

## Command

```bash
echo "127.0.0.1 a.com" | sudo tee -a /etc/hosts
```

## Description

This command appends a DNS mapping to the /etc/hosts file, overriding DNS resolution for a.com to point to localhost (127.0.0.1). Used in PoCs to simulate cross-origin redirects locally without external network dependencies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `127.0.0.1` | IP address to map the hostname to | Yes |
| `a.com` | Hostname to override | Yes |

## Examples

### Basic Usage

```bash
echo "127.0.0.1 example.com" | sudo tee -a /etc/hosts
```

### Advanced Usage

```bash
echo "192.168.1.100 internal.server" | sudo tee -a /etc/hosts
```

## Expected Output

The command echoes the added line and confirms the append operation; no errors if sudo succeeds. Verify with `cat /etc/hosts` to see the new entry.

## Related

- [[Related Procedure]]
