---
id: proc-phabricator-csrf-extract-001
name: Extract-Phabricator-CSRF-Token
tags:
  - csrf
  - token-extraction
  - phabricator
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
updated_at: '2025-12-14T17:27:03.796Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Phabricator-CSRF-Token

## Summary

This procedure outlines logging into Phabricator to extract the Anti-CSRF token from an active session, which can later be tested for persistence across logouts.

## Description

In Phabricator, CSRF tokens are embedded in forms or sessions to prevent cross-site request forgery. Due to timer-based rotation, these tokens are not invalidated on logout. This procedure focuses on capturing the token during an authenticated session via browser inspection, setting up for reuse exploitation. The target environment is a web-based Phabricator instance, and success enables token replay for unauthorized actions.

## Requirements

1. Valid Phabricator credentials
2. Web browser with developer tools (e.g., Chrome DevTools)
3. Access to https://secure.phabricator.com/ or equivalent instance

## Defense

Defensive measures and detection strategies:

- Tie CSRF tokens strictly to user sessions and invalidate on logout
- Implement short-lived tokens with session binding
- Monitor for anomalous form submissions with outdated tokens

## Objectives

1. Capture a valid CSRF token for reuse testing
2. Verify token presence in authenticated requests
3. Prepare for session rotation validation

## Instructions

### Step 1: Authenticate to Phabricator

**Context**: Log in to establish an active session where the CSRF token is generated.

Access the login page and authenticate using provided credentials. No specific command is needed; use the web interface.

> Upon successful login, the session is active, and forms will include the Anti-CSRF token.

### Step 2: Inspect and Extract Token

**Context**: Locate and copy the CSRF token from a form or network request.

Open browser developer tools (F12), navigate to a page with a form (e.g., settings or task creation), and inspect the HTML for input fields named like `__csrf__` or similar. Alternatively, check network tab for requests containing the token in headers or body.

> Expected output: Token value, e.g., a long alphanumeric string like "abc123def456...". Copy it securely for Step 3 in the chain.

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
- [[phabricator]]
