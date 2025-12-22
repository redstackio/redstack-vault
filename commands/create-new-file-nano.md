---
id: a091ad72-153c-42b5-8dc3-a2d29e047bfd
name: create-new-file-nano
type: command
executor: bash
data: nano $_FILENAME
output: null
created_at: '2023-04-06T03:56:17.742763+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - editing
  - evasion
verified: true
validated: true
---

# Create a New File with Nano

## Command

```bash
nano $_FILENAME
```

## Description

Opens Nano editor to create a new file, suitable for adding hidden payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILENAME | Name of the new file (e.g., .payload.sh) | Yes |

## Examples

### Basic Usage

```bash
nano .hidden_payload.sh
```

## Expected Output

Nano opens empty buffer; Ctrl+O to save, Ctrl+X to exit.

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
