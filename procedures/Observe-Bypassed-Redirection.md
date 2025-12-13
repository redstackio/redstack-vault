---
tags:
  - open-redirect
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-open-redirect]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 52a146f9-a37c-452f-98b0-e14f29e739b7
created_at: '2025-12-13T09:01:26.453Z'
updated_at: '2025-12-13T09:01:26.453Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Bypassed Redirection

## Summary

This procedure verifies the successful bypass of the open redirection warning, confirming direct access to the external SSO URL.

## Description

Post-trigger, observe the final redirection to confirm the exploit. The root cause is weak regex allowing double slash bypass in the URL path. This applies to web platforms with SSO-SAML, with the outcome being validation of the vulnerability for potential phishing.

## Requirements

1. Triggered redirection from previous step
2. Ability to inspect URL or HTTP responses
3. Web browser or tool like curl

## Defense

Defensive measures and detection strategies:

- Patch URL parsers to handle edge cases like double slashes
- Implement warning pages for all external redirects

## Objectives

1. Confirm absence of warning page
2. Verify redirection to target URL
3. Assess exploit impact

## Instructions

### Step 1: Check Final URL

**Context**: Inspect the landed URL after redirection.

**Command** ([[commands/curl-test-open-redirect]]):
```bash
curl -I -L 'https://hackerone.com/users//saml/sign_in?email=teste@snapchat.com&remember_me=true'
```

> This shows the final headers and location, confirming bypass.

### Step 2: Validate No Warning

**Context**: Ensure no intermediate warning page appears.

> Expected: Direct landing on SSO URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-open-redirect]]

## Tools Used



## Tags

- [[open-redirect]]
- [[verification]]
