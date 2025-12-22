---
id: proc-slack-sms-relay
tags:
  - sms
  - relay
  - c2
type: procedure
tools:
  - '[[tools/Netcat]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/Netcat-HTTP-Server]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:27:29.558Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Receive-and-Relay-SMS-Verification-Code

## Summary

This procedure uses a simple HTTP server to receive the SMS code from the attacker's phone and relay it to the victim's browser via a JavaScript callback.

## Description

Upon receiving the SMS code (e.g., 196206) on the attacker's phone after the CSRF addition, the attacker manually responds to the victim's GET /a request with the code in a global variable format. This uses netcat as a listener, bridging the SMS channel to the web attack.

## Requirements

1. Attacker's phone number receiving SMS
2. Netcat installed and running on attacker's machine
3. Victim's JS callback hitting the endpoint

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected HTTP servers on internal networks
- Block outbound connections to unknown IPs from browsers
- Use SMS gateways with anomaly detection for 2FA codes
- Log all 2FA SMS sends and verify legitimacy

## Objectives

1. Capture and forward the verification code
2. Enable auto-verification in victim's session
3. Complete the 2FA hijack chain

## Instructions

### Step 1: Start Netcat Listener

**Context**: Set up a simple HTTP server to wait for the callback.

**Command** ([[commands/Netcat-HTTP-Server]]):
```bash
nc -nlvp 8080
```

> Listens on port 8080; verbose output shows connections.

### Step 2: Relay the Code

**Context**: When SMS arrives and GET /a hits, respond with code.

Manual response: HTTP/1.1 200 OK\n\nscode=196206;

> Victim's JS sets scode for verification form.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Sub-Techniques


## Commands Used

- [[commands/Netcat-HTTP-Server]]

## Tools Used

- [[tools/Netcat]]

## Tags

- [[sms]]
- [[relay]]
