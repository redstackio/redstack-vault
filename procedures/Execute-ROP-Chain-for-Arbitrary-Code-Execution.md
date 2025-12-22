---
id: proc-8
tags:
  - csgo
  - rop
  - rce
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:54.581Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Execute-ROP-Chain-for-Arbitrary-Code-Execution

## Summary

This procedure uses the hijacked RIP to construct a ROP chain that sets up the stack for calling ShellExecuteA, executing an arbitrary system command like spawning calculator.

## Description

With RIP control, chain gadgets from engine.dll (now base known) to pop parameters for ShellExecuteA (e.g., lpFile='calc.exe'), bypassing DEP via return-oriented programming.

## Requirements

1. RIP hijacked from OOB
2. ROP gadgets mapped post-ASLR break

## Defense

- Enable CFG and strict ROP mitigations
- Monitor anomalous calls to ShellExecuteA
- Full ASLR with randomization

## Objectives

1. Pivot execution to ROP
2. Execute payload
3. Achieve RCE

## Instructions

### Step 1: Build and Trigger Chain

**Context**: Server sends follow-up messages to influence stack.

Handled by poc.py with gadget chain.

> Expected output: calc.exe spawns on client.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Python]]

## Tags

- csgo
- rop
- rce
