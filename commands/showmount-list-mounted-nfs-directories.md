---
id: d168c6ee-6aa3-460c-a1ad-9afc025d5776
name: showmount-list-mounted-nfs-directories
type: command
executor: bash
data: showmount -d $_TARGET_IP
output: |-
  root@kali:~# showmount -d 10.10.10.12
  Directories on 10.10.10.12:
  /
created_at: '2019-09-11T21:53:20.838942+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - Network
  - Discovery
verified: true
validated: true
---

# showmount-list-mounted-nfs-directories

## Command

```bash
showmount -d $_TARGET_IP
```

## Description

This command uses the showmount utility to query a remote NFS server for the list of directories currently mounted by NFS clients. It is useful for discovering active NFS mounts during network reconnaissance, helping identify exposed file system paths without needing to mount them.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | The IP address or hostname of the target NFS server | Yes |
| -d | Flag to display only the directory names that are mounted (omits client hostnames) | Built-in |

## Examples

### Basic Usage

```bash
showmount -d 10.10.10.12
```

### Advanced Usage

This command does not support additional flags for filtering; combine with grep for post-processing:

```bash
showmount -d 10.10.10.12 | grep '/home'
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~# showmount -d 10.10.10.12
Directories on 10.10.10.12:
/
```

The output lists mounted directories, such as the root '/' path, indicating potential broad exposure. If no directories are listed, no mounts are active or NFS is not responding.

## Related

- [[procedures/List-NFS-Shares]]
- [[commands/showmount-list-nfs-exports]]
