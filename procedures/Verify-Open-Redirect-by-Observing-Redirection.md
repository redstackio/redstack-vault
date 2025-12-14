---
tags:
  - open-redirect
  - phishing
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 1d552d92-3ec2-4c9d-8aa7-24925707ae6a
created_at: '2025-12-14T17:24:23.353Z'
updated_at: '2025-12-14T17:24:23.353Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify-Open-Redirect-by-Observing-Redirection

## Summary

This procedure verifies the open redirect vulnerability by observing the post-authentication redirection to the arbitrary external URL, confirming the potential for phishing attacks.

## Description

After authentication, the endpoint redirects to the specified origin without validation, landing the user on an external site. This step captures the behavior to prove exploitation, highlighting risks like phishing pages that could harvest tokens or credentials. Applicable to web OAuth flows; success indicates no whitelisting, allowing malicious use.

## Requirements

1. Completed authentication from prior steps
2. Active browser session
3. Target external domain accessible

## Defense

Defensive measures and detection strategies:

- Implement server-side redirect validation to ensure origins match registered OAuth callbacks
- Use referrer checks or state parameters in OAuth to prevent open redirects
- Scan for anomalous redirects in browser developer tools or network logs
- Deploy client-side scripts to block unexpected navigations post-auth

## Objectives

1. Confirm unvalidated redirect execution
2. Assess phishing impact by simulating token theft
3. Validate vulnerability for reporting or exploitation

## Instructions

### Step 1: Monitor and Confirm Redirect

**Context**: Watch the browser behavior after authorization to ensure the redirect occurs to the external site.

No command; observation-based.

1. After clicking 'Authorize' on Facebook, observe the URL change.
2. Note the final landing page (e.g., google.com).
3. Check network tab in browser dev tools for the redirect response.

> The redirect header (e.g., Location: http://google.com) points to the origin, confirming the open redirect without domain checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[open-redirect]]
- [[Phishing]]
- [[verification]]
