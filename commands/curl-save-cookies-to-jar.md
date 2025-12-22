---
id: c-curl-save-cookies
name: curl-save-cookies-to-jar
type: command
executor: bash
data: 'curl -s -c cookie.jar https://www.google.com -o /dev/null'
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.738Z'
platforms:
  - Linux
tags:
  - exploitation
  - http
  - cookies
verified: false
validated: true
submitted: true
---

# curl-save-cookies-to-jar

## Command

```bash
curl -s -c cookie.jar https://www.google.com -o /dev/null
```

## Description

Fetches a website with curl, saves cookies to an existing jar file (triggering permission change in libcurl), runs silently, and discards response body. Used to exploit the cookie jar vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode (no progress or errors) | Yes |
| `-c cookie.jar` | Cookie jar file for saving | Yes |
| `https://www.google.com` | Target URL | Yes |
| `-o /dev/null` | Discard output body | Yes |

## Examples

### Basic Usage

```bash
curl -s -c cookie.jar https://www.google.com -o /dev/null
```

### Advanced Usage

```bash
curl -s -c cookie.jar -H "User-Agent: test" https://example.com -o /dev/null
```

## Expected Output

No visible output; cookies appended to jar with permissions set to 0644.

## Related

- [[commands/ls-check-final-permissions]]
- [[procedures/Save-Cookies-Using-curl-to-Trigger-Permission-Change]]
