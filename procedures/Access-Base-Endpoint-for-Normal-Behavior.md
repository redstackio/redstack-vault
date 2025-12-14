---
tags:
  - recon
  - web
  - baseline
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-base-endpoint-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.391Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e2317c78-b018-4355-b7f1-0b91222219bb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Base-Endpoint-for-Normal-Behavior

## Summary

This procedure establishes the normal behavior of the target /item/ endpoint by accessing the base URL and observing the expected 200 OK response, serving as a baseline for subsequent injection tests.

## Description

In the context of testing for SQL injection on 3d.cs.money's /item/ endpoint (IP: 51.83.253.82), this step involves navigating to http://51.83.253.82/item/default, which returns a page for editing skins. This confirms the endpoint is active and behind Cloudflare WAF, with no anomalies in standard access. Prerequisites include direct IP access and a tool like curl or browser.

## Requirements

1. Network access to target IP (51.83.253.82) on port 80
2. Basic HTTP client (curl or browser)
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Monitor access logs for repeated requests to /item/default
- Implement rate limiting on endpoint access

## Objectives

1. Verify endpoint functionality and response code
2. Establish baseline for injection detection
3. Identify any WAF interference

## Instructions

### Step 1: Send Request to Base Endpoint

**Context**: Access the default item page to confirm normal operation and 200 OK status.

**Command** ([[commands/curl-base-endpoint-access]]):
```bash
curl -i http://51.83.253.82/item/default
```

> This command sends a GET request and displays headers. Expected output includes HTTP/1.1 200 OK and HTML content for skin editing. If 404 or redirect, investigate WAF rules.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-base-endpoint-access]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[web]]
