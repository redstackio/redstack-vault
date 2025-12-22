---
id: proc-uuid-6
name: Execute-CSRF-POC-to-Trigger-Stored-XSS
tags:
  - csrf-execution
  - xss-trigger
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.561Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Execute-CSRF-POC-to-Trigger-Stored-XSS

## Summary

This procedure deploys the CSRF PoC to a victim's browser, forcing login as the attacker and automatically triggering the stored XSS for JS execution in the victim's context.

## Description

Combining CSRF login with stored XSS, the victim views the profile post-auth, executing the payload to steal cookies. Targets phishing delivery of the HTML file.

## Requirements

1. Generated CSRF HTML PoC
2. Victim access (e.g., via email link)
3. Stored XSS payload active

## Defense

Defensive measures and detection strategies:

- Educate users on phishing
- Block auto-submitting forms via CSP
- Audit session creations from CSRF-like requests

## Objectives

1. Force victim authentication
2. Execute stored payload
3. Hijack session data

## Instructions

### Step 1: Save and Host PoC

**Context**: Prepare deliverable file.

Paste HTML into Notepad, save as csrf.html, host on a server or send directly.

> File ready for victim interaction.

### Step 2: Victim Interaction and Trigger

**Context**: Execute chain.

Victim opens file; form submits login, authenticates as attacker, then views profile to run XSS.

> Alert shows victim's cookies; potential exfil.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-execution
- xss-trigger
- session-hijack
