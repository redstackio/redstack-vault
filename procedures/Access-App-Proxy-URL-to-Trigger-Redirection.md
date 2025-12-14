---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - redirection
  - nginx
  - proxy-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.254Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-App-Proxy-URL-to-Trigger-Redirection

## Summary

This procedure accesses the configured Shopify App Proxy URL to proxy a request to the mock backend, triggering NGINX to process the X-Accel-Redirect header and serve internal content.

## Description

By hitting the proxy endpoint, the request reaches the mock server, which injects the redirect header. NGINX, due to misconfiguration, follows it to internal paths like /collections/all. Targets public-facing Shopify stores; verifies the vulnerability. Outcome: Internal content served via proxy.

## Requirements

1. Configured App Proxy from prior procedure
2. Browser or HTTP client
3. Target shop name

## Defense

Defensive measures and detection strategies:

- Patch NGINX to strip X-Accel-Redirect from untrusted proxies
- Log and alert on internal path accesses via proxies
- Require authentication on all internal NGINX locations

## Objectives

1. Proxy request to mock backend
2. Induce NGINX redirection to internal path
3. Observe unauthorized internal access

## Instructions

### Step 1: Navigate to Proxy URL

**Context**: Use a browser to send the proxied request.

Open https://{shop}.myshopify.com/a/apps in a browser, replacing {shop} with the actual shop name (e.g., mytestshop).

> Expected output: Instead of mock response, browser shows Shopify's /collections/all page content.

### Step 2: Verify Redirection

**Context**: Inspect network traffic to confirm header processing.

Use browser dev tools (Network tab) to check the response; look for X-Accel-Redirect in upstream but internal content served.

Alternatively, use curl:

```bash
curl -v https://{shop}.myshopify.com/a/apps
```

> Expected output: Verbose log shows 200 OK with internal page HTML, no direct redirect but content from /collections/all.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- redirection
- nginx
- proxy-trigger
