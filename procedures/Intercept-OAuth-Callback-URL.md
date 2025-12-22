---
tags:
  - csrf
  - oauth
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[SSH]]'
updated_at: '2025-12-14T17:27:03.679Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c90fe254-ffc1-442f-bab5-97bc7602340a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[SSH]]'
---
# Intercept OAuth Callback URL

## Summary

Intercepts the OAuth callback to capture the authorization code without completing the flow on the attacker's side.

## Description

Using a proxy, the attacker drops the callback request to Shopify's endpoint, extracting the code for reuse in the victim's session. This exploits the CSRF vulnerability. Target: https://pinterest-commerce.shopifyapps.com/auth/pinterest/callback.

## Requirements

1. Proxy tool like Burp Suite configured
2. Browser traffic routed through proxy
3. Fresh OAuth code from prior step

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens or state params in redirects
- Monitor for dropped or unusual callback requests in logs

## Objectives

1. Capture code parameter
2. Prevent attacker-side completion
3. Prepare malicious link

## Instructions

### Step 1: Set Up Proxy

**Context**: Route traffic.

Configure browser to use Burp proxy on localhost:8080.

> Expected: All requests intercepted.

### Step 2: Intercept and Drop

**Context**: Capture during redirect.

When callback hits, view in Burp, copy URL (e.g., ?code=d0c18854a3359866774d479614081453d235962f), then drop the request.

> Expected: Full URL saved, no completion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[SSH]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[oauth]]
- [[interception]]
