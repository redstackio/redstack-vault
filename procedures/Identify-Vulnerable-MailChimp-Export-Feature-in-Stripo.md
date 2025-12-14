---
tags:
  - clickjacking
  - recon
  - oauth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f78d055d-e931-43f1-b68d-b64f9c3ca11e
created_at: '2025-12-14T17:28:05.387Z'
updated_at: '2025-12-14T17:28:05.387Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Vulnerable-MailChimp-Export-Feature-in-Stripo

## Summary

This procedure involves navigating to Stripo's MailChimp export page to identify the vulnerable OAuth authorization endpoint that lacks frame-busting protections, confirming susceptibility to clickjacking for credential theft.

## Description

In the context of testing Stripo's integration with MailChimp, access the export feature at my.stripo.email, which redirects to MailChimp's OAuth page. This page does not implement X-Frame-Options or CSP frame-ancestors, allowing it to be embedded in iframes on malicious sites. The procedure verifies this by observing the redirect and testing iframe embeddability, setting the stage for phishing attacks where users unwittingly enter credentials.

## Requirements

1. Web browser access to my.stripo.email
2. Basic knowledge of browser developer tools for inspecting redirects and headers
3. No authentication required for initial navigation

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN on OAuth pages
- Use CSP with frame-ancestors 'none' to prevent embedding
- Monitor for unusual redirects or iframe attempts in web logs

## Objectives

1. Confirm the OAuth endpoint's vulnerability to iframing
2. Document the exact redirect URL and parameters for PoC development
3. Establish the attack surface for credential phishing

## Instructions

### Step 1: Navigate to Export Page

**Context**: Access Stripo's MailChimp export interface to trigger the vulnerable redirect.

Open a browser and go to https://my.stripo.email, then select the export to MailChimp option. This will redirect to the OAuth authorization page.

> The redirect targets https://login.mailchimp.com/oauth2/authorize?response_type=code&client_id=350877244304&redirect_uri=https%3A%2F%2Fmy.stripo.email%2Fcabinet%2Fexportservice%2Fv1%2Fmailchimpauth.html%3FaccountId%3D2085372, where users enter username and password.

### Step 2: Inspect for Frame Protections

**Context**: Verify the absence of anti-framing headers using browser tools.

In the browser's developer console (F12), check the Network tab for the response headers on the OAuth page. Look for X-Frame-Options or Content-Security-Policy.

> Expected: No restrictive headers, allowing the page to be iframed. Test by creating a simple local HTML with <iframe src="[OAuth URL]"></iframe> to confirm it loads without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[recon]]
- [[oauth]]
