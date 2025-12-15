---
tags:
  - open-redirect
  - phishing
  - redirection
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
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:23.457Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 0d85c03a-7a30-4d9a-9d41-28b7520b5ae0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Redirect-After-Authentication

## Summary

This procedure simulates or observes the completion of social authentication on a Weblate endpoint with a malicious 'next' parameter, resulting in redirection to an external site.

## Description

After a user authenticates via a social provider on the crafted URL, Weblate processes the 'next' parameter and redirects without validation, sending the now-authenticated user to the attacker's site. This can lead to phishing for additional credentials or exploitation of the session. Applicable to all affected providers.

## Requirements

1. Crafted malicious URL from previous step.
2. Victim interaction: User must click and authenticate.
3. Attacker control over the redirect target (e.g., phishing page on evil.com).

## Defense

Defensive measures and detection strategies:

- Enforce redirect validation post-authentication.
- Use referrer checks or tokens to prevent open redirects.
- Alert on redirects to external domains after login.

## Objectives

1. Complete authentication flow.
2. Confirm redirection to malicious site.
3. Capture any leaked session data or enable further attacks.

## Instructions

### Step 1: Lure Victim to URL

**Context**: Deliver the malicious link to the target.

Send the URL via phishing email or other vector, prompting the user to log in via social auth.

> Expected output: User accesses the endpoint.

### Step 2: Complete Authentication

**Context**: User performs social login.

The user selects the provider (e.g., Facebook) and authenticates on the external social site, granting access to Weblate.

> Expected output: Callback to Weblate with auth success.

### Step 3: Observe Redirection

**Context**: Verify the post-auth redirect.

Monitor the browser or network tab; upon success, the app redirects to ///evil.com instead of internal pages.

> Expected output: HTTP 302 to malicious domain; user lands on phishing site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[redirection]]
