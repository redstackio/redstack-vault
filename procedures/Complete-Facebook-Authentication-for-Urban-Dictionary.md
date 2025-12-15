---
tags:
  - open-redirect
  - oauth
  - authentication
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
id: 82329bb7-31c8-49a0-b1c5-677c0e380dbf
created_at: '2025-12-14T17:24:23.357Z'
updated_at: '2025-12-14T17:24:23.357Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Complete-Facebook-Authentication-for-Urban-Dictionary

## Summary

This procedure completes the Facebook OAuth authentication process for Urban Dictionary, authorizing the app and triggering the open redirect to the manipulated origin URL after successful login.

## Description

Following initiation with a manipulated origin, this step involves logging into Facebook and granting permissions to Urban Dictionary. Due to the vulnerability, the post-auth redirect uses the unvalidated origin, sending the user (and any auth tokens) to an external site. This is exploitable in phishing by tricking victims into authenticating via a crafted link. The environment is browser-based OAuth, with outcomes including token exposure if the external site is malicious.

## Requirements

1. Valid Facebook account credentials
2. Prior access to the manipulated auth endpoint
3. Browser session from Step 1

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect URI validation in OAuth callbacks, rejecting external origins
- Require user confirmation before redirects in authentication flows
- Log and alert on OAuth authorizations with suspicious origins
- Integrate OAuth provider checks (e.g., Facebook's app review) to flag insecure redirects

## Objectives

1. Authenticate and authorize to trigger the vulnerable redirect
2. Demonstrate token leakage potential to external domains
3. Enable phishing by completing the flow on victim behalf

## Instructions

### Step 1: Perform Facebook Login and Authorization

**Context**: Use provided credentials to log in and approve the app connection, which processes the origin parameter.

No command; interactive browser steps.

1. Enter Facebook username and password on the login page.
2. Review and accept permissions for Urban Dictionary (e.g., profile access).
3. Confirm the connection.

> Upon approval, the OAuth callback executes the redirect to the origin URL, bypassing any internal validation.

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
- [[oauth]]
- [[authentication]]
