---
data: 'curl -I https://www.periscope.tv/'
tags:
  - recon
  - headers
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-05T00:00:00Z'
updated_at: '2025-12-14T17:28:12.574Z'
id: a90de195-941b-4284-845e-8a8670101d5d
verified: false
validated: true
submitted: true
---
# curl-fetch-headers

## Command

```bash
curl -I https://www.periscope.tv/
```

## Description

This command uses curl to perform a HEAD request on the target URL, retrieving only the HTTP response headers without downloading the body. It is useful for reconnaissance to inspect security headers like X-Frame-Options during vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I, --head` | Fetch headers only | Yes |
| `URL` | Target URL to inspect | Yes |

## Examples

### Basic Usage

```bash
curl -I https://www.periscope.tv/
```

### Advanced Usage

```bash
curl -I -H "User-Agent: Mozilla/5.0" https://www.periscope.tv/
```

## Expected Output

HTTP/1.1 200 OK
Server: nginx
X-Frame-Options: ALLOW-FROM https://twitter.com/
... (other headers)

Successful run shows status 200 and the vulnerable header value.

## Related

- [[Related Procedure: Inspect-HTTP-Response-Headers-for-X-Frame-Options]]
