---
id: uuid-proc-3
tags:
  - token-exfiltration
  - csrf-theft
  - post-exfil
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration to Cloud Storage]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:15.677Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration to Cloud Storage]]'
  - '[[Steal Web Session Cookie]]'
---
# Exfiltrate-CSRF-Token-to-Attacker-Domain

## Summary

This procedure captures the CSRF token sent in the POST request to the attacker-controlled domain, enabling subsequent forgery of authenticated requests to the target Rails application.

## Description

The exfiltrated token arrives via the POST body or headers (X-CSRF-Token). As it's session-bound, it allows the attacker to perform CSRF-protected actions like updating profiles or transferring funds. In XSS contexts, this bypasses CSP by avoiding script execution. The vulnerability stems from no proper validation of href before token addition and weak regex not handling leading whitespace.

## Requirements

1. Successful POST from prior step
2. Server-side logging for incoming requests
3. Knowledge of target app's CSRF-protected endpoints
4. Tools to replay requests with the stolen token

## Defense

Defensive measures and detection strategies:

- Rotate CSRF tokens frequently or per-request
- Implement token binding to specific actions/endpoints
- Monitor for unusual POSTs to external domains from app JS
- Use WAF rules to block space-prefixed URLs in attributes

## Objectives

1. Receive and extract the valid CSRF token
2. Validate token usability on target
3. Enable chained attacks like unauthorized actions

## Instructions

### Step 1: Capture Incoming POST

**Context**: Log the request on attacker server to extract the token.

Server endpoint receives POST; parse headers for `X-CSRF-Token` (e.g., in Python Flask: `request.headers.get('X-CSRF-Token')`). Store the 32-char token.

### Step 2: Verify Token Validity

**Context**: Test the token by sending a benign POST to a protected target endpoint.

Use curl or similar to replay:

```bash
curl -X POST https://target.com/protected -H "X-CSRF-Token: stolen_token" -d "data= test"
```

Success if no 403 CSRF error.

### Step 3: Execute Follow-on Attack

**Context**: Use token for malicious actions.

Craft POST to sensitive endpoints, e.g., change email: include token in header and required params.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exfiltration to Cloud Storage]] Exfiltration Over Web Service
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[token-exfiltration]]
- [[csrf-theft]]
- [[post-exfil]]
