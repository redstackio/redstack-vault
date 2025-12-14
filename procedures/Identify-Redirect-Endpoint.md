---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - recon
  - xss
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-redirect-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:39.355Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Redirect-Endpoint

## Summary

This procedure involves probing the TikTok Ads portal to identify endpoints where the 'redirect' parameter is reflected without sanitization, setting the stage for XSS and iframe injection attacks.

## Description

In the TikTok Ads portal, certain endpoints process redirect URLs passed via the 'redirect' parameter. Due to lack of input validation, attacker-supplied values are directly embedded into the HTML response, enabling reflected attacks. This step focuses on reconnaissance to confirm reflection, typically using HTTP requests to observe response behavior in a browser or proxy tool.

## Requirements

1. Access to a web proxy like Burp Suite for intercepting and inspecting requests
2. Knowledge of the target endpoint (e.g., ads.tiktok.com login or callback URLs)
3. Basic HTTP request crafting capabilities

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts and iframes
- Sanitize and URL-encode all user inputs in redirect parameters
- Monitor for anomalous redirect patterns in server logs

## Objectives

1. Confirm reflection of the 'redirect' parameter in HTML output
2. Identify lack of sanitization for scripts or HTML tags
3. Prepare payloads for subsequent exploitation steps

## Instructions

### Step 1: Probe Endpoint with Basic Redirect

**Context**: Send a simple request to check if the parameter is reflected.

**Command** ([[commands/curl-redirect-test]]):
```bash
curl -X GET "https://ads.tiktok.com/some-endpoint?redirect=https://example.com" -v
```

> This command fetches the endpoint and verbose output shows if 'https://example.com' appears unescaped in the response body, indicating vulnerability.

### Step 2: Inspect Response in Browser

**Context**: Load the URL in a browser to verify client-side rendering.

**Command** (Manual browser test):

Open the crafted URL in a browser and inspect the page source for reflected content.

> Expected: Parameter value visible in HTML without encoding, allowing further payload testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-redirect-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[recon]]
- [[xss]]
