---
id: cmd-uuid-001
data: cat /etc/hosts
tags:
  - file-read
  - recon
type: command
output: "127.0.0.1\tlocalhost\n255.255.255.255\tbroadcasthost\n::1             localhost\nfe80::1%lo0\tlocalhost"
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.089Z'
verified: false
validated: true
submitted: true
---
# cat-etc-hosts

## Command

```bash
cat /etc/hosts
```

## Description

Displays the contents of the /etc/hosts file, which maps hostnames to IP addresses locally. Used in this exploit to demonstrate file read access via AppleScript in the malicious .app.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /etc/hosts | Path to the hosts file | Yes |

## Examples

### Basic Usage

```bash
cat /etc/hosts
```

### Advanced Usage

```bash
cat /etc/hosts | grep localhost
```

## Expected Output

Contents of /etc/hosts file, such as:

127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost

## Related

- [[Related Procedure: Host-Malicious-AppleScript-App-on-NFS-Mount]]
