---
id: proc-identify-open-redirect-1245165
tags:
  - open-redirect
  - discovery
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:26:21.932Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify Open Redirect in IDP Authorize Endpoint

## Summary

This procedure tests and confirms an open redirect vulnerability in the /api/2/idp/authorize/ endpoint of Acronis Cloud, where the state parameter allows redirection to arbitrary external domains without validation.

## Description

The endpoint handles OAuth-like authorization flows and reflects the user-controlled state parameter directly into the Location header of a 302 redirect response. No validation or domain allowlisting is performed, enabling attackers to redirect users (or resource fetches) to malicious sites. This is particularly exploitable when chained with resource loading like CSS. The procedure targets web applications and requires browser testing. Outcomes include verifiable redirects to external URLs.

## Requirements

1. Browser with developer tools
2. Access to https://mc-beta-cloud.acronis.com
3. Optional: curl or similar for non-interactive testing

## Defense

Defensive measures and detection strategies:

- Validate redirect targets against an allowlist of trusted domains
- Use strict referrer policies and CSP to limit redirect impacts
- Log and alert on redirects to external domains

## Objectives

1. Verify lack of validation on state parameter
2. Demonstrate arbitrary domain redirection
3. Assess chaining potential with resource loads

## Instructions

### Step 1: Construct Test URL

**Context**: Build a request to the authorize endpoint with a controllable state pointing to an external domain.

Use this URL: https://mc-beta-cloud.acronis.com/api/2/idp/authorize/?client_id=fb2bf44e-ac14-444a-b2a9-e5e81fe73b80&redirect_uri=%2Fhci%2Fcallback&response_type=code&scope=openid&state=http://localhost&nonce=bhgjuvrrvpwauibleqhvfqat

> Replace http://localhost with any test domain you control.

### Step 2: Trigger and Observe Redirect

**Context**: Load the URL in the browser and inspect the response.

Open Network tab, visit the URL, and check the response headers for Location: http://localhost (or your test).

> If the browser follows to the external site, the vulnerability is confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- open-redirect
- discovery
