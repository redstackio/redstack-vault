---
tags:
  - xss
  - flash
  - verification
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
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d707faf5-c68d-4968-81ea-2ca4c6b45de5
created_at: '2025-12-14T03:16:14.578Z'
updated_at: '2025-12-14T03:16:14.578Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-SharedObject-Setting-with-Confirm-Dialog

## Summary

This verification procedure confirms the successful poisoning of the Flash SharedObject by monitoring for execution indicators, such as a JavaScript confirm dialog triggered by the malicious cached SWF during or immediately after the initial load.

## Description

After loading the poisoning URL, the set_shared_con.swf caches the malicious t2.swf and sets the SharedObject. If the player attempts to load Conviva components, it may immediately execute the cached SWF, calling JavaScript via ExternalInterface. This step observes the outcome to ensure persistence and functionality before proceeding to the trigger phase. It targets environments where Flash local storage is writable and ExternalInterface is permitted.

## Requirements

1. Browser with Flash enabled from the previous procedure
2. No additional setup; relies on the SharedObject state
3. Ability to inspect browser console for Flash errors

## Defense

Defensive measures and detection strategies:

- Block or audit Flash SharedObject access via browser extensions (e.g., FlashBlock)
- Clear Flash storage regularly or use incognito mode for testing
- Detect unexpected JS dialogs from Flash content in application logs
- Enforce no Flash policy files that restrict ExternalInterface

## Objectives

1. Confirm SharedObject modification without errors
2. Validate malicious SWF caching and initial execution
3. Ensure setup for delayed XSS trigger

## Instructions

### Step 1: Wait for Flash Execution

**Context**: Allow time for the SWF to fully load, cache the malicious URL, and potentially execute the JS payload.

Pause for 10-30 seconds after accessing the poisoning URL. No action required beyond observation.

> Flash operations are asynchronous; waiting ensures the SharedObject flush completes.

### Step 2: Observe Confirmation

**Context**: Look for indicators of successful JS execution from the malicious SWF.

Monitor the browser for a confirm dialog displaying 'moin: [current domain]'.

**Expected Output**: Pop-up confirm dialog appears, confirming domain context and ExternalInterface success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[flash]]
- [[verification]]
