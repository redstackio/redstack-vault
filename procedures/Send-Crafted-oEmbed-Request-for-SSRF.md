---
tags:
  - ssrf
  - exploitation
  - ghost-cms
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/get-oembed-ssrf-request]]'
platforms:
  - Web
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2f3cf303-e018-41cf-a3b7-eda1ca3ecbc8
created_at: '2025-12-14T04:39:09.665Z'
updated_at: '2025-12-14T04:39:09.665Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Crafted-oEmbed-Request-for-SSRF

## Summary

This procedure exploits the SSRF vulnerability in Ghost's oEmbed endpoint by sending an authenticated GET request with a URL using a spoofed hostname (e.g., spoofed.burpcollaborator.net) that resolves to 127.0.0.1, bypassing regex-based validation.

## Description

The fetchOembedData() function in Ghost validates URLs using HTTP_REGEX for protocol and hostname patterns for localhost/IPv4/IPv6, but does not resolve the hostname. Domains like localtest.me pass the checks yet point to localhost, allowing the server to fetch internal resources. Requires publisher role authentication.

## Requirements

1. Authenticated session cookie from Ghost admin
2. Proxy tool like Burp Suite for request crafting
3. Local listener running to capture SSRF traffic

## Defense

Defensive measures and detection strategies:

- Implement hostname resolution in SSRF checks
- Log and monitor oEmbed endpoint requests for suspicious URLs
- Restrict API access to trusted roles

## Objectives

1. Trigger SSRF to access localhost/internal services
2. Bypass existing SSRF mitigations
3. Demonstrate arbitrary GET request capability

## Instructions

### Step 1: Craft and Send Request

**Context**: Use Burp Repeater to send the oEmbed request with a bypassing URL.

**Command** ([[commands/get-oembed-ssrf-request]]):
```bash
GET /ghost/api/v3/admin/oembed/?url=http://spoofed.burpcollaborator.net/index.html&type=embed HTTP/1.1
Host: localhost:2368
Cookie: ghost-admin-api-session=your-session-cookie
```

> Include full headers for authentication. Expected output: JSON oEmbed response from Ghost, but internally fetches the spoofed URL resolving to localhost.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/get-oembed-ssrf-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[exploitation]]
- [[ghost-cms]]
