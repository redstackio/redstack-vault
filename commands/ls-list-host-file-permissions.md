---
type: command
executor: bash
data: ls -la /etc/shadow
platforms:
  - Linux
tags:
  - verification
  - file-permissions
verified: true
validated: true
---

# ls-list-host-file-permissions

## Command

```bash
ls -la $_FILE_PATH
```

## Description

Lists the permissions and details of a host file (e.g., /etc/shadow) to verify changes post-container escape. Use this on the host to confirm success indicators like altered setuid or world-access bits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Path to the file on host (e.g., /etc/shadow) | Yes |

## Examples

### Basic Usage

```bash
ls -la /etc/shadow
```

### Advanced Usage

```bash
ls -la /etc/passwd /etc/shadow
```

## Expected Output

For success after escape:
```
-rwsrwsrwx 1 root shadow 1209 Oct 10  2019 /etc/shadow
```

Normal (pre-escape): `-rw-r----- 1 root shadow ...`. The 'rws' indicates setuid/world-write, confirming compromise.

## Related

- [[procedures/Container-Escape-Using-Device-File]]
