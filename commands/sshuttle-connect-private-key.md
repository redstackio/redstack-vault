---
id: f27ab0a3-5a81-4ac0-a237-7b0d0a2f8694
name: sshuttle-connect-private-key
type: command
executor: bash
data: sshuttle -vvr $_USER@$_PIVOT_HOST $_SUBNET -e "ssh -i $_KEY_PATH"
output: null
created_at: '2023-04-06T03:56:22.695008+00:00'
updated_at: '2023-04-10T20:25:19.583732+00:00'
platforms:
  - Linux
tags:
  - pivoting
  - sshuttle
  - authentication
verified: true
validated: true
---

# sshuttle-connect-private-key

## Command

```bash
sshuttle -vvr $_USER@$_PIVOT_HOST $_SUBNET -e "ssh -i $_KEY_PATH"
```

## Description

Establishes an sshuttle tunnel using private key authentication for the SSH connection to the pivot host, ideal for passwordless setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -vv | Verbose logging | No |
| -r | Remote host | Yes |
| $_USER | SSH username | Yes |
| $_PIVOT_HOST | Pivot IP/hostname | Yes |
| $_SUBNET | Target subnet | Yes |
| -e | Custom SSH command | Yes |
| $_KEY_PATH | Path to private key file | Yes |

## Examples

### Basic Usage

```bash
sshuttle -vvr root@10.10.10.10 10.1.1.0/24 -e "ssh -i ~/.ssh/id_rsa"
```

### Advanced Usage

With additional SSH options:

```bash
sshuttle -vvr root@10.10.10.10 10.1.1.0/24 -e "ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no"
```

## Expected Output

"Using key for authentication...\nSSH tunnel active\nTraffic forwarding enabled for 10.1.1.0/24"

## Related

- [[procedures/network-pivoting-with-sshuttle]]
- [[tools/sshuttle]]
