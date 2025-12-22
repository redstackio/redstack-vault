---
id: 13788446-141c-4a61-810b-798fa61d2689
name: open-existing-file-nano
type: command
executor: bash
data: nano $_FILENAME
output: null
created_at: '2023-04-06T03:56:17.742813+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - editing
  - evasion
verified: true
validated: true
---

# Open an Existing File with Nano

## Command

```bash
nano $_FILENAME
```

## Description

Opens an existing file in Nano for editing obfuscated content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILENAME | Path to existing file | Yes |

## Examples

### Basic Usage

```bash
nano .existing_payload.sh
```

## Expected Output

Nano loads file contents; edit as needed.

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
