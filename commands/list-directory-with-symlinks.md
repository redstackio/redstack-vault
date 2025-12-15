---
data: ls -lash
tags:
  - inspection
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-25T00:00:00Z'
updated_at: '2025-12-14T17:24:08.337Z'
id: 0d823480-0db9-45ae-9eef-ff5ff54b3238
verified: false
validated: true
submitted: true
---
# list-directory-with-symlinks

## Command

```bash
ls -lash
```

## Description

Lists directory contents in long format with human-readable sizes, including hidden files, to inspect symlinks and file structures during export modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Include all files, including hidden | Yes |
| `-l` | Long format with details | Yes |
| `-s` | Display size in blocks | Yes |
| `-h` | Human-readable sizes | Yes |

## Examples

### Basic Usage

```bash
ls -lash
```

### Advanced Usage

```bash
ls -lash /path/to/export
```

## Expected Output

Directory listing like '8 lrwxr-xr-x 1 user staff 11B Oct 25 20:43 VERSION -> /etc/passwd', showing symlink details.

## Related

- [[commands/create-tar-gz-archive]]
