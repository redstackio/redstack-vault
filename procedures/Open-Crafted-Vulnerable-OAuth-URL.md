---
tags:
  - open-redirect
  - url-manipulation
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:23.061Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ec008fad-28e6-4974-a774-a73086f13f01
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Open-Crafted-Vulnerable-OAuth-URL

## Summary

This procedure involves navigating to a specially crafted URL that exploits the open redirection in Phabricator's OAuth flow by using backslashes to bypass forward slash validation, loading the login page primed for phishing.

## Description

The vulnerability on secure.phabricator.com allows attackers to manipulate the redirect parameter in the OAuth endpoint. By replacing forward slashes with backslashes in the URL, validation checks (likely whitelisting or path normalization) are evaded, enabling redirection to arbitrary sites post-authentication. This step sets up the phishing vector for token theft.

## Requirements

1. Access to the crafted URL (e.g., from https://www.dropbox.com/s/e8r08b52hawc65c/OAuth.txt)
2. Incognito browser session active
3. Internet access to reach secure.phabricator.com

## Defense

Defensive measures and detection strategies:

- Enforce strict URL validation in OAuth redirects, normalizing paths and rejecting backslashes
- Use Content Security Policy (CSP) to restrict post-auth redirects
- Log and alert on anomalous redirect parameters in web traffic

## Objectives

1. Load the Phabricator login page with manipulated redirect
2. Confirm the vulnerability triggers without errors
3. Position for OAuth provider selection

## Instructions

### Step 1: Retrieve and Paste URL

**Context**: The crafted URL contains the open redirect payload, targeting the OAuth login endpoint.

No command required; download or copy the URL from the source file, then paste it into the incognito address bar and press Enter.

> Expected output: The secure.phabricator.com login page loads, with the URL parameter intact (e.g., redirect=\\malicious-site.com).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- open-redirect
- oauth-bypass
