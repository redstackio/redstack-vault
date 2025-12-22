---
id: efdfad3b-6385-461c-a4b9-ea0d222ea7eb
name: open-file-vim
type: command
executor: bash
data: vim $_FILE
output: null
created_at: '2023-04-06T03:56:17.742632+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - editing
  - evasion
verified: true
validated: true
---

# Open a File in Vim

## Command

```bash
vim $_FILE
```

## Description

Launches the Vim editor to open or create a file for editing hidden payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE | Path to the file (e.g., .hidden.sh) | Yes |

## Examples

### Basic Usage

```bash
vim /tmp/.payload.sh
```

### Create New

```bash
vim newfile.sh
```

## Expected Output

Vim editor opens with file contents; use :wq to save and quit.

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
