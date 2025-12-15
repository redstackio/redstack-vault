---
data: cat flag
tags:
  - verify
  - leak
type: command
executor: bash
platforms:
  - Linux
id: 9d85b8c2-a1b9-4be2-9cff-c0f1c0d8b74c
created_at: '2025-12-14T17:24:19.383Z'
updated_at: '2025-12-14T17:24:19.383Z'
verified: false
validated: true
submitted: true
---
# cat-flag-verify

## Command

```bash
cat flag
```

## Description

Displays contents of the exploited 'flag' file to verify overwrite with cookie data or leak success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| flag | Path to the protected/exploited file | Yes |

## Examples

### Basic Usage

```bash
cat /etc/passwd  # For real /etc/passwd overwrite
```

### Advanced Usage

```bash
cat flag | grep "Netscape"  # Check for cookie headers
```

## Expected Output

File contents, e.g., # Netscape HTTP Cookie File
#HttpOnly_... (131 bytes if exploited).

## Related

- [[tools/cat]]
- [[procedures/Verify-Exploit-Success]]
