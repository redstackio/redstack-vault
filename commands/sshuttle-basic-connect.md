---
id: 439cbd87-5d1c-4745-adee-e57459795bd5
name: sshuttle-basic-connect
type: command
executor: bash
data: sshuttle -vvr $_USER@$_PIVOT_HOST $_SUBNET
output: null
created_at: '2023-04-06T03:56:22.694933+00:00'
updated_at: '2023-04-10T20:25:19.583732+00:00'
platforms:
  - Linux
tags:
  - pivoting
  - sshuttle
  - connect
verified: true
validated: true
---

# sshuttle-basic-connect

## Command

```bash
sshuttle -vvr $_USER@$_PIVOT_HOST $_SUBNET
```

## Description

Establishes a basic sshuttle tunnel to forward traffic for a specified subnet through an SSH connection to the pivot host. This is the core command for initiating network pivoting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -vv | Verbose output level (two -v for detailed logging) | No |
| -r | Specify remote host for SSH connection | Yes |
| $_USER | Username for SSH authentication | Yes |
| $_PIVOT_HOST | IP or hostname of the pivot host | Yes |
| $_SUBNET | Target internal subnet to tunnel (e.g., 10.1.1.0/24) | Yes |

## Examples

### Basic Usage

```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24
```

### Advanced Usage

Add DNS tunneling with `--dns`:

```bash
sshuttle -vvr user@10.10.10.10 10.1.1.0/24 --dns
```

## Expected Output

"Starting sshuttle.\nRemote host: user@10.10.10.10\nForwarding for: 10.1.1.0/24\nClient interface: tun0\nConnected."

## Related

- [[procedures/network-pivoting-with-sshuttle]]
- [[tools/sshuttle]]
