---
id: b4b29e65-8e29-4d76-b4bc-d55f3e281c11
name: Identify-Vulnerable-Shopify-Partner-API-Endpoint
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.421Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - csrf
  - shopify
  - api
  - recon
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---

# Identify-Vulnerable-Shopify-Partner-API-Endpoint

## Summary

This procedure involves discovering and verifying a CSRF-vulnerable endpoint in the Shopify Partner API that allows exporting installed app users via simple GET requests without protection.

## Description

In a web-based environment targeting Shopify's partner dashboard, this procedure tests API endpoints for missing CSRF protections. The specific endpoint https://app.shopify.com/services/partners/api_clients/{app_id}/export_installed_users processes GET requests to download sensitive user installation data. By sending unauthenticated requests from a browser session, attackers confirm the lack of CSRF tokens, enabling cross-site exploitation. Prerequisites include access to a browser and knowledge of a target app ID.

## Requirements

1. Browser with developer tools for testing requests
2. Knowledge of a target Shopify app ID
3. Network access to Shopify's partner domain

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing or data-exporting endpoints
- Monitor for anomalous GET requests to export endpoints from non-partner IPs
- Enable browser security headers like SameSite cookies

## Objectives

1. Confirm endpoint vulnerability to CSRF
2. Gather details on response format for exploitation planning
3. Validate no authentication barriers beyond session cookies

## Instructions

### Step 1: Prepare Test Environment

**Context**: Set up a browser session authenticated as a Shopify partner to simulate victim conditions.

Log in to the Shopify Partner Dashboard at https://app.shopify.com and ensure session cookies are active.

### Step 2: Test Endpoint Directly

**Context**: Send a manual GET request to the endpoint to check for CSRF enforcement.

Open browser developer tools (F12), navigate to the Network tab, and load a page or use the console to issue:

```javascript
fetch('https://app.shopify.com/services/partners/api_clients/{app_id}/export_installed_users', {method: 'GET'})
  .then(response => response.text())
  .then(data => console.log(data));
```

Replace {app_id} with a valid app ID. If the request succeeds without CSRF errors, the endpoint is vulnerable.

> This JavaScript fetch mimics a cross-site request; success indicates missing protection. Expected output: CSV or JSON data of installed users.

### Step 3: Verify Lack of Protections

**Context**: Confirm no tokens or checks are required.

Attempt the same request from an incognito window or external tool like curl (without cookies) to ensure session-based auth is the only barrier.

```bash
curl -X GET "https://app.shopify.com/services/partners/api_clients/{app_id}/export_installed_users"
```

> Without cookies, it should fail auth but not CSRF; with cookies from authenticated session, it succeeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[api]]
- [[recon]]
