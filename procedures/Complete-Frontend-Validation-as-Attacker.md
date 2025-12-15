---
tags:
  - validation
  - frontend
  - csrf
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:27:57.845Z'
sub_techniques: []
id: d59011d2-379e-4ec0-a0ec-db214508cc29
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Complete-Frontend-Validation-as-Attacker

## Summary

This procedure allows the attacker to finalize the integration on the frontend by simulating a successful callback, convincing the UI that the OAuth flow completed legitimately despite the CSRF forgery.

## Description

After the victim's interaction links the account, the attacker manually navigates to the callback URL to trigger postMessage communication with the iframe. This bypasses any frontend checks, making the integration appear active in the HackerOne dashboard without alerting the victim.

## Requirements

1. Authentication ID from crafted URL
2. Attacker's browser session on HackerOne
3. Access to integration-configuration domain

## Defense

Defensive measures and detection strategies:

- Implement iframe sandboxing and origin checks
- Verify callback parameters server-side
- Monitor for manual navigations to callbacks

## Objectives

1. Trick frontend into success state
2. Activate integration UI
3. Prepare for GraphQL exploitation

## Instructions

### Step 1: Obtain Callback URL

**Context**: Use the Auth ID to construct callback.

Form the URL: https://hackerone.integration-configuration.com/auth/cb?id=<Auth ID>.

### Step 2: Navigate to Callback

**Context**: Trigger the postMessage to iframe.

In the attacker's browser, change window location to the callback URL while on the integrations page.

```javascript
// Simulated via console
window.location.href = 'https://hackerone.integration-configuration.com/auth/cb?id=<Auth ID>';
```

> This sends success message to the parent window.

### Step 3: Verify UI Update

**Context**: Confirm integration shows as linked.

Check the HackerOne integrations dashboard for the new active integration.

**Expected Output**: No errors; integration listed as successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[validation]]
- [[frontend]]
- [[csrf]]
