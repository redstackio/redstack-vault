---
data: >-
  curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=450"
  -H "Cookie: JSESSIONID=session_cookie" -v
tags:
  - web
  - test
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.398Z'
id: 16202779-6075-42f8-8912-62bbd10f2d8f
verified: false
validated: true
submitted: true
---
# curl-test-message-id

## Command

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=450" -H "Cookie: JSESSIONID=session_cookie" -v
```

## Description

This command probes a specific message ID to determine if it's valid by attempting deletion and checking the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `messageID=450` | ID to test | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=450" -H "Cookie: JSESSIONID=def456"
```

### Advanced Usage

```bash
curl -X GET "https://community.informatica.com/pm-delete.jspa?messageID=450" -H "Cookie: JSESSIONID=def456" --max-time 10
```

## Expected Output

Success: 200/302; Invalid: 404/400 or error message.

## Related

- [[Related Procedure: Determine-Target-Message-IDs]]
