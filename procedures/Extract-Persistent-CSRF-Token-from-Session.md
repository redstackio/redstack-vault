---
id: proc-uuid-1
tags:
  - csrf
  - token-extraction
  - web
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
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:27:22.965Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract Persistent CSRF Token from Session

## Summary

This procedure extracts the CSRF authenticity token from an active web session on a shared workstation, exploiting the fact that the token does not regenerate after login, allowing it to remain valid for subsequent users.

## Description

In vulnerable web applications, the CSRF token (often called 'authenticity token') is generated once and persists across sessions on the same browser instance without regeneration upon login. This is particularly exploitable in shared environments like public computers. The attacker logs in temporarily, extracts the token via browser inspection, and leaves it for reuse. This enables crafting attacks that bypass CSRF protections. Prerequisites include physical access to the workstation and knowledge of the application's token placement, typically in hidden form fields or headers.

## Requirements

1. Physical access to a shared workstation with the target web application loaded
2. A temporary valid login credential for the application
3. Browser with developer tools enabled (e.g., Chrome DevTools)

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens on every login or session start
- Implement per-session token binding to user accounts
- Monitor for anomalous token reuse in logs on shared systems
- Use short-lived tokens and workstation session isolation

## Objectives

1. Obtain a valid, persistent CSRF token for reuse
2. Confirm token stability across simulated logouts/logins
3. Prepare token for integration into malicious requests

## Instructions

### Step 1: Access the Application Session

**Context**: Log in to establish a session where the token is present and persistent.

Log in to the target web application using provided credentials. Navigate to a page with a protected form (e.g., profile settings).

**Expected Output**: Active session with forms loaded.

### Step 2: Inspect and Extract Token

**Context**: Use browser tools to locate and copy the token without triggering regeneration.

Right-click on a form element and select 'Inspect Element'. Search for input fields named 'authenticity', '_token', or similar hidden fields. Copy the value attribute of the token field.

For example, in the HTML source:

```html
<input type="hidden" name="authenticity" value="abc123def456ghi789">
```

Copy "abc123def456ghi789" to a secure note.

**Expected Output**: Token string extracted.

### Step 3: Verify Persistence

**Context**: Test that the token remains unchanged after logout/login simulation.

Log out and log back in (or simulate by clearing non-token cookies). Re-inspect the form to confirm the token value is identical.

**Expected Output**: Token unchanged, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-extraction]]
- [[web]]
