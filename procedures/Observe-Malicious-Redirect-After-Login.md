---
id: proc-uuid-003
tags:
  - redirect
  - exploitation
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.524Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe-Malicious-Redirect-After-Login

## Summary

This procedure verifies and exploits the post-login redirect to an arbitrary external site, confirming the open redirect vulnerability and enabling further phishing actions.

## Description

After authentication, the Fabric.io server processes the 'redirect_url' parameter and redirects the browser to the prefixed domain (e.g., @evil-site.com becomes evil-site.com). This bypasses any internal redirect logic, sending the now-authenticated user to the attacker's site. In a real attack, this leads to fake login prompts for credential theft or drive-by downloads. Testing in modern browsers like Firefox or Chrome confirms the behavior across environments.

## Requirements

1. Successful authentication from prior step
2. Browser developer tools or network monitoring to observe the redirect
3. Attacker-controlled site to receive the redirected traffic

## Defense

Defensive measures and detection strategies:

- Enforce redirect validation post-authentication, rejecting external or untrusted URLs
- Use HTTP response headers like Content-Security-Policy to restrict navigation
- Analyze server logs for redirect patterns to external domains and flag anomalies

## Objectives

1. Trigger and observe the unintended redirect
2. Confirm bypass of domain restrictions
3. Harvest data or deliver payload on the destination site

## Instructions

### Step 1: Complete Login Submission

**Context**: Ensure authentication triggers the redirect logic.

Submit the form as in the previous procedure.

> Server authenticates and initiates redirect. Expected output: Brief success page or direct HTTP 302 to external site.

### Step 2: Monitor Browser Navigation

**Context**: Watch for the redirect in the browser or dev tools.

Open browser dev tools (F12) and check the Network tab.

> The redirect request appears as a 302 response to the malicious domain. Expected output: Browser loads the external site seamlessly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- [[redirect]]
- [[exploitation]]
