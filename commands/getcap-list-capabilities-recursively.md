---
id: 346e563b-ca14-4d8d-b240-42d4503d6a7b
name: getcap-list-capabilities-recursively
type: command
executor: bash
data: getcap -r $_DIRECTORY
output: null
created_at: '2023-04-06T03:56:18.861432+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - capabilities
  - privilege-escalation
verified: true
validated: true
---

# getcap-list-capabilities-recursively

## Command

```bash
ggetcap -r $_DIRECTORY
```

## Description

This command recursively lists file capabilities in the specified directory on Linux systems. Capabilities are extended attributes granting specific privileges to executables, useful for discovering escalation paths without full root access. Use it during privilege escalation reconnaissance to identify abuseable binaries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DIRECTORY | Target directory path (e.g., /usr/bin, /bin) to scan recursively | Yes |
| -r | Enable recursive listing of capabilities in subdirectories | Yes |

## Examples

### Basic Usage

Scan /usr/bin for capabilities:

```bash
ggetcap -r /usr/bin
```

### Advanced Usage

Scan the entire root filesystem (may take longer and require broader access):

```bash
ggetcap -r /
```

## Expected Output

Successful execution produces a list of files with capabilities, formatted as `path/to/file = cap_name+flags`. Example:

```
/usr/bin/ping = cap_net_raw+ep
/usr/bin/dumpcap = cap_dac_override,cap_net_admin,cap_net_raw+eip
```

If no capabilities are found, the output is empty. Errors may occur if the directory is inaccessible.

## Related

- [[procedures/Linux-List-Capabilities-of-Executables]]
