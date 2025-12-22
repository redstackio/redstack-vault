---
tags:
  - execution
  - clickjacking
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Electron
  - Desktop
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:41.642Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 95e4f6d1-cfa5-485f-a4b4-f80912aa91f0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Payload-Execution-via-Page-Load

## Summary

This procedure triggers the injected prototype pollution payload by loading or refreshing the affected page in the Rocket.Chat desktop client, dispatching a synthetic click event to invoke the bypassed onclick handler.

## Description

Once injected, the payload waits for page load to execute. The counter ensures the bypass activates after 3 normal regex tests (e.g., during UI interactions), then dispatches a MouseEvent 'click' on the crafted <a> element. This calls electron.shell.openExternal with the arbitrary URL, such as a file:// path to launch a host application.

## Requirements

1. Payload injected and DOM ready
2. Desktop client webview loaded on vulnerable page
3. No CSP blocking event dispatch

## Defense

Defensive measures and detection strategies:

- Validate all click events and hrefs server-side before rendering
- Disable or restrict openExternal in Electron preload scripts
- Log synthetic events and anomalous external opens

## Objectives

1. Dispatch click to trigger onclick handler
2. Bypass remaining checks for external call
3. Invoke electron.shell.openExternal with malicious URL

## Instructions

### Step 1: Load the Malicious Page

**Context**: Navigate to the chat or report page containing the XSS-injected payload.

In the desktop client, browse or send a message that triggers the vulnerable rendering.

> Page loads; payload executes automatically on DOMContentLoaded or inline.

### Step 2: Confirm Event Dispatch

**Context**: Verify the synthetic click fires without user interaction.

Add console.log to payload: `console.log('Click dispatched');` before dispatchEvent.

> Console output confirms; no visible user click needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[webview]]
