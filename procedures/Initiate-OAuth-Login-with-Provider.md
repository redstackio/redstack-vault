---
tags:
  - oauth
  - authentication
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:23.046Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fc9380c5-80cc-4a83-bde0-c664ea74e471
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Initiate-OAuth-Login-with-Provider

## Summary

This procedure selects an OAuth provider on the Phabricator login page to start the external authentication process, which is necessary to trigger the vulnerable redirect after approval.

## Description

Once the crafted URL loads the login page, choosing a provider like Disqus redirects to its authorization endpoint. This step is key in the phishing attack, as it lures the victim into providing credentials, setting up the token theft upon return to Phabricator.

## Requirements

1. Loaded Phabricator login page from vulnerable URL
2. Valid account on the selected OAuth provider (e.g., Disqus)
3. Active incognito session

## Defense

Defensive measures and detection strategies:

- Require user confirmation for OAuth authorizations
- Implement rate limiting on login attempts from suspicious URLs
- Scan for phishing domains mimicking legitimate OAuth flows

## Objectives

1. Begin the OAuth handshake with the provider
2. Redirect to provider's login for credential entry
3. Maintain the manipulated redirect state

## Instructions

### Step 1: Select Provider

**Context**: This engages the OAuth flow, passing the vulnerable redirect back to Phabricator post-auth.

No command required; click the "Login with Disqus" (or Facebook) button on the page.

> Expected output: Browser redirects to the Disqus (or chosen provider) authorization page, prompting for login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- oauth-login
- provider-selection
