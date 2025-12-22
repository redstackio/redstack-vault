---
id: e48dca51-ab6f-4b35-a1bf-5d41795ace8f
name: preview-first-lines-head
type: command
executor: bash
data: head -n $_LINES $_FILE
output: null
created_at: '2023-04-06T03:56:17.742380+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - file-viewing
  - evasion
verified: true
validated: true
---

# Preview First Lines with Head

## Command

```bash
head -n $_LINES $_FILE
```

## Description

Prints the first few lines of a file, helpful for quickly checking the start of an obfuscated script without full disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -n $_LINES | Number of lines to show (default 10) | No |
| $_FILE | Path to the file | Yes |

## Examples

### Basic Usage

```bash
head -n 5 /tmp/script.sh
```

### Default Lines

```bash
head /tmp/script.sh
```

## Expected Output

First lines of the file, e.g.:
```
==> /tmp/script.sh <==
# Generated config
Line 2
```

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
