---
tags:
  - stack-overflow
  - tls
  - wolfssl
type: procedure
tools:
  - '[[tools/SSL-Labs-Scanner]]'
  - '[[tools/Netcat]]'
  - '[[tools/XXD]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:31.141Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1c16919c-8963-45d9-9f2f-a3c5f84fabac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Triggering Stack Buffer Overflow in WolfSSL

## Summary

This procedure uses server scanners and crafted TLS handshakes to overflow a fixed-size array in WolfSSL's ClientHello parsing, causing server crashes and potential RCE on non-ASLR systems.

## Description

WolfSSL parses signature hash algorithm lists into a 32-element array without bounds checks, allowing >32 algorithms to overflow the stack. Compile WolfSSL with ASAN to detect; trigger via SSL Labs or netcat PoC sending large lists. Targets TLS servers on Linux.

## Requirements

1. WolfSSL server compiled with ASAN
2. Network access to target server
3. Hex editor for payload crafting
4. No specific credentials

## Defense

Defensive measures and detection strategies:

- Add bounds checks in TLS parsers
- Monitor for unusual ClientHello sizes
- Use ASLR and stack canaries

## Objectives

1. Overflow stack array in parsing
2. Cause server crash
3. Enable potential RCE

## Instructions

### Step 1: Scan with SSL Labs

**Context**: Trigger overflow remotely.

**Command** (No direct command; use tool):
Use [[tools/SSL-Labs-Scanner]] against WolfSSL server.

> Sends >32 algorithms; ASAN reports stack-buffer-overflow.

### Step 2: Craft PoC with Netcat and XXD

**Context**: Manual crash reproduction.

**Command** (Custom bash PoC):
Use netcat to send hex-crafted ClientHello with large hash list (generate hex via xxd).

> Server crashes on oversized input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None extracted

## Tools Used

- [[tools/SSL-Labs-Scanner]]
- [[tools/Netcat]]
- [[tools/XXD]]

## Tags

- stack-overflow
- tls-parsing
