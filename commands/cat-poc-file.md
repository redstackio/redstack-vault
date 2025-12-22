---
data: cat frogs-find-bugs/hehehe
tags:
  - view-file
  - poc
type: command
output: '''EdOverflow :D'''
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.991Z'
id: 44aa64cc-35af-46fb-946c-75879e1185d0
verified: false
validated: true
submitted: true
---
# cat-poc-file

## Command

```bash
cat frogs-find-bugs/hehehe
```

## Description

Displays the contents of the injected PoC file to confirm successful payload extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `frogs-find-bugs/hehehe` | Path to the file | Yes |

## Examples

### Basic Usage

```bash
cat frogs-find-bugs/hehehe
```

### Advanced Usage

```bash
cat frogs-find-bugs/hehehe | grep keyword
```

## Expected Output

File contents printed to stdout, e.g., 'EdOverflow :D' for PoC.

## Related

- [[Related Procedure: Download-and-Extract-Malicious-Tarball]]
