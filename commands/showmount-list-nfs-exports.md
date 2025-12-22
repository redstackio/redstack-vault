---
type: command
executor: bash
platforms:
  - Linux
tags:
  - network
  - discovery
verified: true
validated: true
---

# showmount-list-nfs-exports

## Command

```bash
showmount -e $_TARGET_IP
```

## Description

This command queries a remote NFS server to list all exported file systems (shares) configured on the target. It reveals which directories are available for mounting over the network and to which clients, aiding in identifying misconfigured shares during discovery phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the target NFS server | Yes |
| -e | Flag to display the list of NFS exports (shared directories and access permissions) | Built-in |

## Examples

### Basic Usage

```bash
showmount -e 10.10.10.10
```

### Advanced Usage

Pipe output to grep for specific exports:

```bash
showmount -e 10.10.10.10 | grep '*'
```

## Expected Output

```
root@kali:~# showmount -e 10.10.10.10
Export list for 10.10.10.10:
/ *
```

The output shows exported paths followed by allowed clients (e.g., '*' means world-accessible). An empty list or error indicates no exports or access denial.

## Related

- [[procedures/List-NFS-Shares]]
- [[commands/showmount-list-mounted-nfs-directories]]
