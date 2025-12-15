---
data: echo 'RCE demonstrated successfully' > /tmp/proof.txt
tags:
  - rce
  - benign
  - demonstration
type: command
output: File /tmp/proof.txt created with content 'RCE demonstrated successfully'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.260Z'
id: d124083a-6b54-48ad-b78f-a87059af7d7e
verified: false
validated: true
submitted: true
---
# execute-benign-rce-command

## Command

```bash
echo 'RCE demonstrated successfully' > /tmp/proof.txt
```

## Description

This command executes a harmless echo to a temporary file on the target web server, used in RCE demonstrations to prove code execution without causing damage. It is injected via the Apache Struts vulnerability payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `echo` | Outputs the specified string | Yes |
| `'RCE demonstrated successfully'` | The benign message to write | Yes |
| `> /tmp/proof.txt` | Redirects output to a temp file | Yes |

## Examples

### Basic Usage

```bash
echo 'RCE demonstrated successfully' > /tmp/proof.txt
```

### Advanced Usage

```bash
echo 'Vulnerability confirmed at $(date)' >> /tmp/proof.txt
```

## Expected Output

The command creates or appends to /tmp/proof.txt with the message, confirming successful remote execution. In a demonstration, this may be verified through server logs or response changes.

## Related

- [[Related Procedure: Demonstrate-RCE-with-Custom-Script]]
