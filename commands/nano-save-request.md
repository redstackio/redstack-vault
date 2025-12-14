---
id: cmd-nano-testsql
data: nano testsql.txt
tags:
  - editor
  - file-save
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.913Z'
verified: false
validated: true
submitted: true
---
# nano-save-request

## Command

```bash
nano testsql.txt
```

## Description

Opens the nano text editor to create or edit the file testsql.txt, used for pasting and saving a captured HTTP request from Burp Suite in the context of SQL injection preparation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| testsql.txt | Filename to open or create for the HTTP request | Yes |

## Examples

### Basic Usage

```bash
nano testsql.txt
```

### Advanced Usage

```bash
nano -w testsql.txt
```

> The -w flag disables word wrapping for long HTTP lines.

## Expected Output

Nano editor interface opens. Paste content (e.g., HTTP request), save with Ctrl+O, confirm filename, exit with Ctrl+X. No output if successful; file created/updated.

## Related

- [[Related Procedure: Save-Captured-Request-for-Exploitation]]
