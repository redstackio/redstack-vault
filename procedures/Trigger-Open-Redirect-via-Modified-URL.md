---
tags:
  - open-redirect
  - phishing
  - shopify
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:30.542Z'
sub_techniques: []
id: 5a83eaf0-4723-4ec8-ba8d-44fbb551947a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Open-Redirect-via-Modified-URL

## Summary

This procedure activates the exploited open redirect by accessing the modified search URL on the Shopify dev site, resulting in an unauthorized redirection to an external domain due to the 'result_url' bypass.

## Description

After modifying the URL, this final step involves loading it in a browser, where the /search/result endpoint processes the request. The root cause is improper handling of '@' in 'result_url', allowing the server to interpret the external domain as the redirect target without validating against shopify.dev restrictions. This confirms the vulnerability and demonstrates its use in social engineering, such as embedding in phishing links. Impact includes potential user deception, though Shopify noted it requires interaction and thus low severity.

## Requirements

1. Modified URL from previous procedure
2. Web browser
3. Optional: Developer tools to inspect redirects

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect policies with full URL parsing and domain checks
- Block or sanitize special characters like '@' in redirect parameters
- Implement CSP headers to limit navigations

## Objectives

1. Execute the redirect to verify exploitation
2. Observe the bypass in action
3. Assess potential for phishing integration

## Instructions

### Step 1: Load Modified URL

**Context**: Direct the browser to the crafted URL to initiate the request.

Paste the full modified URL into the address bar and press Enter.

> Server receives the request and begins processing the search result simulation.

### Step 2: Observe Redirect Behavior

**Context**: Monitor the navigation as the vulnerability triggers.

The page may briefly load a Shopify result page before redirecting.

> Due to '@www.facebook.com', it redirects externally to Facebook (or chosen domain).

### Step 3: Verify Success

**Context**: Confirm the external site loads, proving the open redirect.

Check the final URL in the browser; it should be the external domain.

> Successful if no Shopify error and external page appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[redirect]]
- [[exploit]]
