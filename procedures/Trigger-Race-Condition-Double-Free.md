---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
name: Trigger-Race-Condition-Double-Free
tags:
  - race-condition
  - double-free
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/actionscript-race-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:18.618Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Race-Condition-Double-Free

## Summary

This procedure triggers the race condition in Adobe Flash Player by having one worker call bytearray.compress() while another accesses the shared ByteArray, leading to improper synchronization and a double free vulnerability as described in CVE-2015-0312.

## Description

The attack scenario targets Flash Player's multi-threaded worker environment where shared ByteArrays are not adequately synchronized. By precisely timing the compress() call in one worker against an access (e.g., readByte()) in another, Flash mishandles the object, resulting in a double free. This is exploitable in browsers like Chrome for memory corruption. Prerequisites include the setup from the previous procedure and timing precision (e.g., via loops or delays). Expected outcomes: Observable double free via crashes or heap debugging.

## Requirements

1. Loaded SWF from setup procedure with active workers
2. Vulnerable Flash Player in browser
3. Ability to execute ActionScript in workers (e.g., via message passing)
4. Debugging tools like Chrome DevTools or Flash debugger

## Defense

Defensive measures and detection strategies:

- Update to patched Flash versions
- Use browser policies to block unsigned SWFs
- Detect multi-worker Flash usage via behavioral analysis in security tools

## Objectives

1. Induce the race condition through concurrent operations
2. Confirm double free occurrence
3. Prepare for memory exploitation

## Instructions

### Step 1: Implement Race in Worker Scripts

**Context**: Extend worker code to perform the conflicting operations.

**Code Snippet** ([[commands/actionscript-race-trigger]]):

```actionscript
// Worker1.as
byteArray.compress(CompressionAlgorithm.DEFLATE);

// Worker2.as
import flash.utils.ByteArray;
var byteArray:ByteArray = Worker.current.getSharedProperty("byteArray");
byteArray.position = 0;
byteArray.readByte(); // Race with compress
```

> Starts the compress and access concurrently. Expected output: Synchronization failure leading to double free.

### Step 2: Execute in Browser

**Context**: Load and run the updated SWF to trigger the race.

**Instructions**: Refresh the HTML page with the SWF; use JavaScript to send messages to workers if needed for timing.

> Expected output: Flash process instability or error logs indicating memory issues.

### Step 3: Validate Double Free

**Context**: Use debugging to confirm the vulnerability.

**Instructions**: Attach a debugger (e.g., FlashDevelop) and monitor heap; look for freed object reuse.

> Expected output: Evidence of double free in heap dumps.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/actionscript-race-trigger]]

## Tools Used


## Tags

- [[race-condition]]
- [[double-free]]
