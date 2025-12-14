---
id: proc-intercept-shopify-request
tags:
  - race-condition
  - http-interception
  - shopify
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/configure-burp-proxy]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.622Z'
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
# Intercept-Shopify-Location-Creation-Request

## Summary

This procedure captures the HTTP request for creating a new store location in Shopify using a proxy tool, enabling subsequent replay for race condition exploitation.

## Description

In the context of Shopify's store management, the location creation process sends a POST request to an API endpoint like /admin/api/locations.json. By intercepting this request, attackers can analyze and duplicate it to send multiple concurrent versions, bypassing the system's limit checks due to lack of synchronization. This is typically performed in a merchant's browser session with valid credentials, targeting web-based e-commerce platforms.

## Requirements

1. Valid Shopify merchant account with location creation permissions
2. Installed proxy tool like Burp Suite for HTTP interception
3. Local network setup to route browser traffic through the proxy

## Defense

Defensive measures and detection strategies:

- Implement client-side request signing or nonces to prevent replay attacks
- Monitor for unusual spikes in concurrent API requests from the same session
- Use rate limiting on location creation endpoints

## Objectives

1. Capture the exact payload and headers for location creation
2. Identify the API endpoint and authentication mechanism
3. Prepare for concurrent request flooding

## Instructions

### Step 1: Configure Proxy Tool

**Context**: Set up Burp Suite to intercept traffic from the browser to Shopify.

**Command** ([[commands/configure-burp-proxy]]):
```bash
# No direct command; configure via Burp UI: Set proxy listener on 127.0.0.1:8080
```

> Launch Burp Suite, enable intercept in the Proxy tab, and configure your browser (e.g., Firefox) to use the proxy at 127.0.0.1:8080. Expected output: Browser traffic routed through Burp.

### Step 2: Trigger Location Creation

**Context**: Perform the action in Shopify dashboard to capture the request.

**Command** ([[commands/navigate-shopify-dashboard]]):
```bash
# Browser action: Log in to Shopify admin, go to Settings > Locations > Add location, fill form, and submit
```

> With intercept enabled, submit the form. Burp will pause on the POST request. Inspect and forward it. Expected output: Captured request with JSON payload like {"location":{"name":"Test","address1":"123 Street"}} and headers including X-Shopify-Access-Token.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/configure-burp-proxy]]
- [[commands/navigate-shopify-dashboard]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- race-condition
- http-interception
- shopify
