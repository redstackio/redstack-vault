---
id: proc-uuid-4
tags:
  - xss
  - javascript-execution
  - externalinterface
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:27.054Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-JavaScript-Execution-via-Unescaped-Metadata

## Summary

This procedure monitors and confirms the execution of arbitrary JavaScript injected through unescaped RTMP metadata in the VideoJS SWF, demonstrating the XSS impact like popping a confirm dialog.

## Description

Once the SWF connects to the RTMP stream, it parses metadata (ID3 tags and server info) into a JS object and passes it via ExternalInterface.call, e.g., console.log("plugin","loadedmetadata",({tags:({TIT2:"payload"}})). The unescaped payload executes in the browser context. Attack scenario: Observe in dev tools or UI; target environment: Flash-enabled page; expected outcomes include visible JS effects like alerts, enabling further attacks like session theft.

## Requirements

1. Loaded SWF from previous procedure
2. Browser dev tools open
3. Payload designed for execution (e.g., confirm dialog)

## Defense

Defensive measures and detection strategies:

- Escape all strings in ExternalInterface calls
- Use JSON.parse with safe handlers for metadata
- Browser extensions to block Flash JS interactions
- Anomaly detection on JS execution patterns in media contexts

## Objectives

1. Capture unescaped metadata in JS calls
2. Verify payload execution (e.g., dialog or console output)
3. Assess impact like data exfiltration potential

## Instructions

### Step 1: Open Dev Tools

**Context**: Prepare to monitor JS execution.

In browser, open console (F12) and watch for console.log or UI changes.

**Expected Output**: Ready for event monitoring.

### Step 2: Trigger and Observe

**Context**: Let the SWF process the stream to invoke ExternalInterface.

Wait for autoplay to connect and read metadata.

**Expected Output**: Console shows: try { flash toXML(console.log("plugin","loadedmetadata",({audiochannels:2,tags:({TIT2:"\")}})}finally{confirm(/moin/)}//"})) } – executing the confirm.

### Step 3: Validate Impact

**Context**: Confirm arbitrary code runs in page context.

Look for confirm dialog with 'moin' or custom payload effect.

> Success if dialog appears, proving XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[javascript-execution]]
- [[xss]]
