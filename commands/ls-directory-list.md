---
id: cmd-ls-dir-001
data: ls -la /var/run/ /proc/
tags:
  - recon
  - file-system
type: command
output: |-
  drwxr-xr-x 2 root root 4096 Oct 1 12:00 ubnt-session
  dr-xr-xr-x 300 root root 0 Oct 1 12:00 1234
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.954Z'
verified: false
validated: true
submitted: true
---
# ls-directory-list

## Command

```bash
ls -la /var/run/ /proc/
```

## Description

Lists directory contents with detailed permissions to identify exposed files in EdgeOS file-system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Long format | Yes |
| `-a` | All files | Yes |
| Path | Target directory | Yes |

## Examples

### Basic Usage

```bash
ls -la /var/run/
```

### Advanced Usage

```bash
ls -la /var/run/ | grep ubnt
```

## Expected Output

Permissions and ownership details, e.g., readable files owned by root but accessible to operator.

## Related

- [[commands/cat-file-read]]
