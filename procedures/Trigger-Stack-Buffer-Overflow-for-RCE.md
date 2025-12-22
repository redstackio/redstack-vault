---
id: proc-trigger-buffer-overflow
tags:
  - buffer-overflow
  - rce
  - stack-overflow
type: procedure
tools:
  - '[[tools/poc-py]]'
  - '[[tools/PuTTY-PSCP]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:30:58.701Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Dynamic-link Library Injection]]'
---
# Trigger-Stack-Buffer-Overflow-for-RCE

## Summary

This procedure details the server-side delivery of a crafted file size payload during SCP transfer, exploiting unsafe parsing in PuTTY PSCP to overwrite the stack buffer and achieve remote code execution on the client.

## Description

Once the client authenticates and requests file transfer, the malicious server responds with an oversized file size string (e.g., 1000+ bytes of 'A's followed by shellcode or ROP chain) in the SSH packet. PuTTY's sscanf call without bounds checking overflows a local stack buffer, allowing EIP overwrite (e.g., to 0x41414141 for proof-of-concept). This affects Windows clients with PuTTY <=0.66, dating back ~9 years. Outcomes include memory corruption, crash, or controlled execution; attach a debugger like WinDbg to verify EIP control.

## Requirements

1. Active malicious SSH server from prior procedure
2. Connected vulnerable client in transfer state
3. Optional: Debugger on client for verification

## Defense

Defensive measures and detection strategies:

- Enable ASLR/DEP on Windows to hinder exploitation
- Log and alert on SSH transfer anomalies (e.g., large file sizes)
- Use endpoint detection to monitor PuTTY process crashes

## Objectives

1. Overflow stack buffer via crafted SSH response
2. Overwrite EIP for code execution control
3. Confirm RCE through crash analysis or payload exec

## Instructions

### Step 1: Monitor Client Transfer Request

**Context**: Wait for the client's SCP request post-auth; the PoC server detects this automatically.

Observe server console for incoming transfer init.

### Step 2: Deliver Overflow Payload

**Context**: Server sends malformed file size (e.g., "AAAA..." exceeding buffer) to trigger sscanf overflow.

The [[tools/poc-py]] handles this; no manual command. Customize payload in poc.py for specific shellcode if needed (e.g., edit response buffer to include ROP gadgets).

**Expected Output**: Client PuTTY process corrupts; EIP=0x41414141 in memory dump.

### Step 3: Verify Exploitation

**Context**: Analyze client crash for success.

Use WinDbg: `!analyze -v` on crash dump to confirm stack overwrite.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Dynamic-link Library Injection]] Dynamic-link Library Injection (via overflow)

### Sub-Techniques

- N/A

## Commands Used


## Tools Used

- [[tools/poc-py]]
- [[tools/PuTTY-PSCP]]

## Tags

- buffer-overflow
- rce
- stack-overflow
