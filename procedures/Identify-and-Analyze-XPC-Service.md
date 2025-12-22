---
id: proc-xpc-identify-001
tags:
  - xpc
  - mach-service
  - reverse-engineering
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Process Discovery]]'
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:29:10.024Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
  - '[[System Information Discovery]]'
---
# Identify-and-Analyze-XPC-Service

## Summary

This procedure identifies the Mach service name used by Kaspersky Internet Security's system extension for XPC connections and analyzes the authorization handler to confirm improper client verification, enabling subsequent unauthorized access.

## Description

In the context of exploiting Kaspersky Internet Security on macOS, this involves examining the Info.plist of the system extension (SEXT) to extract the NEMachServiceName key, revealing '2Y8XE5CQ94.com.kaspersky.kav.sysext'. Further, disassembling the IPCService class's shouldAcceptNewConnection: method shows it only verifies the caller's Team ID via processIdentifier comparison to an expected string, lacking checks for bundle ID, entitlements, or audit_token to prevent PID reuse. This flaw allows any process with the same Team ID to connect, facilitating AV control.

## Requirements

1. Local access to macOS Big Sur with KIS installed
2. Reverse engineering tools like Hopper or Ghidra for disassembly
3. Ability to inspect bundle Info.plist files

## Defense

Defensive measures and detection strategies:

- Implement full XPC authorization using xpc_connection_get_pid and audit_token checks
- Monitor for unexpected XPC connections to system services via EndpointSecurity framework
- Enforce minimum macOS version and bundle ID validation in shouldAcceptNewConnection

## Objectives

1. Extract Mach service name for targeting
2. Confirm authorization weakness for exploit planning
3. Identify protocols like FileMonitorProtocol for control

## Instructions

### Step 1: Extract Mach Service Name

**Context**: Locate the XPC service endpoint in the system extension bundle.

No specific command; manually open /Library/SystemExtensions/com.kaspersky.kav.sysext.sysext/Contents/Info.plist and search for NEMachServiceName.

> Expected output: Value '2Y8XE5CQ94.com.kaspersky.kav.sysext'.

### Step 2: Disassemble Authorization Handler

**Context**: Analyze the IPCService class to verify the flaw.

Use a disassembler on the SEXT binary to inspect shouldAcceptNewConnection:.

> Expected output: Code snippet showing [r15 processIdentifier] compared only to Team ID string, no further validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Process Discovery]] Process Discovery (via processIdentifier)
- [[System Information Discovery]] System Information Discovery (Team ID extraction)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xpc
- reverse-engineering
- macos
