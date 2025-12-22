---
id: cmd-ls-malicious-dir
data: ls
tags:
  - listing
  - verification
type: command
output: >-
  Shows total 8, -rw-rw-r-- amazing-movie.mp4, -rw-rw-r-- README.txt, drwxrwxr-x
  tls
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.810Z'
verified: false
validated: true
submitted: true
---
# list-directory-contents

## Command

```bash
ls
```

## Description

List contents of current directory to verify POC files before triggering the snap exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
ls
```

### Advanced Usage

```bash
ls -la
```

## Expected Output

Shows total 8, -rw-rw-r-- amazing-movie.mp4, -rw-rw-r-- README.txt, drwxrwxr-x tls.

## Related

- [[commands/change-to-malicious-directory]]
- [[procedures/Prepare-Malicious-Directory-for-Snap-RCE]]
