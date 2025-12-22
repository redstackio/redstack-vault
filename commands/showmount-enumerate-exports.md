---
id: 65fd5f36-31be-4122-bf9d-9c7049dafc92
name: showmount-enumerate-exports
type: command
executor: bash
data: showmount -e $_TARGET_IP
output: null
created_at: '2023-04-06T03:56:19.323020+00:00'
updated_at: '2023-04-10T20:34:35.902057+00:00'
platforms:
  - Linux
tags:
  - nfs
  - enumeration
verified: true
validated: true
---

# showmount-enumerate-exports

## Command

```bash
showmount -e $_TARGET_IP
```

## Description

This command queries an NFS server to list all exported file systems (shares) and their access permissions. It is used during reconnaissance to identify mountable shares that may be vulnerable to exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the NFS server | Yes |
| -e | Flag to show export list (built-in) | Yes |

## Examples

### Basic Usage

```bash
showmount -e 10.10.10.10
```

### Advanced Usage

```bash
showmount -e nfs-server.example.com
```

## Expected Output

```
Export list for 10.10.10.10:
/shared *
/home 192.168.1.0/24
```

A successful response lists shares; empty or "clnt_create: RPC: Program not registered" indicates no NFS service or firewall block.

## Related

- [[procedures/Linux-Privilege-Escalation-via-NFS-Root-Squashing]]
