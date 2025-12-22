---
id: 434dbf77-0df1-4f74-a15e-c3bf90385219
name: display-file-contents-cat
type: command
executor: bash
data: cat $_FILE
output: null
created_at: '2023-04-06T03:56:17.742264+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - file-viewing
  - evasion
verified: true
validated: true
---

# Display File Contents with Cat

## Command

```bash
cat $_FILE
```

## Description

Displays the entire contents of a specified file to the terminal, useful for verifying hidden payloads or scripts during evasion activities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE | Path to the file to display (e.g., .hidden.sh) | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/.payload.sh
```

### With Multiple Files

```bash
cat file1.txt file2.txt
```

## Expected Output

The raw contents of the file printed to stdout, e.g.:
```
# Obfuscated comment
malicious_command
```

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
