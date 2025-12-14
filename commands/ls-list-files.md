---
data: ls
tags:
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.391Z'
id: 47d2719e-6ee8-44bd-a14c-db5c00e27a85
verified: false
validated: true
submitted: true
---
# ls-list-files

## Command

```bash
ls
```

## Description

Lists files in the current directory to verify malicious file creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard ls with no flags | No |

## Examples

### Basic Usage

```bash
ls
```

### Advanced Usage

```bash
ls -la
``` (for detailed view)

## Expected Output

Displays filenames, including the malicious one: ""><object src=1 onerror="javascript:alert(1);">Controlling what is documented here

## Related

- [[commands/touch-malicious-filename]]
- [[procedures/Verify-Malicious-File-Creation]]
