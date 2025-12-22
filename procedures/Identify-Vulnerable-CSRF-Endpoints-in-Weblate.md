---
id: proc-weblate-csrf-identify
tags:
  - csrf
  - weblate
  - endpoint-analysis
  - recon
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
updated_at: '2025-12-14T17:27:23.352Z'
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
# Identify Vulnerable CSRF Endpoints in Weblate

## Summary

This procedure involves analyzing Weblate's HTTP requests to identify translation lock and unlock endpoints that are vulnerable to CSRF due to using unprotected GET requests, enabling reconnaissance for potential exploitation in web applications.

## Description

In Weblate, translation components can be locked or unlocked to manage collaborative access. By inspecting network traffic during these actions, attackers discover that endpoints like /lock/ and /unlock/ use GET methods without CSRF tokens, allowing cross-site forgery. This procedure targets web-based translation platforms like Weblate, requiring an authenticated session for observation. Expected outcomes include confirmation of vulnerability, setting the stage for disruption without direct interaction.

## Requirements

1. Access to a Weblate instance as an authenticated user with translation permissions.
2. Browser with developer tools (e.g., Chrome DevTools) for network inspection.
3. Basic knowledge of HTTP requests and CSRF mechanics.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints.
- Enforce POST for sensitive actions and monitor for anomalous GET requests to admin paths.
- Use web application firewalls (WAF) to detect cross-site requests lacking referer headers.

## Objectives

1. Discover unprotected state-changing endpoints in translation management.
2. Verify absence of CSRF protections to assess exploitability.
3. Gather details for crafting malicious requests.

## Instructions

### Step 1: Authenticate and Navigate to Translation Component

**Context**: Log in to Weblate and access a specific translation project to prepare for request inspection.

Navigate to the target Weblate instance, authenticate with valid credentials, and go to a translation component URL, such as https://target-weblate.com/aptoide-uploader/strings/ka/.

> This establishes the session context needed for observing authenticated requests.

### Step 2: Inspect Lock and Unlock Requests

**Context**: Use developer tools to capture and analyze HTTP traffic during lock/unlock actions.

Open browser developer tools (F12), switch to the Network tab, and perform a lock action on the component. Repeat for unlock. Examine the requests for paths like /lock/aptoide-uploader/strings/ka/ and /unlock/aptoide-uploader/strings/ka/.

> Look for GET method usage and absence of CSRF tokens (e.g., no _token parameter or header). Successful identification shows state changes via simple GET without protections.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[weblate]]
- [[recon]]
