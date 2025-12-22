---
id: proc-uuid-004
tags:
  - debugger-trigger
  - backtest-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/set-watch-websocket-message]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:23.607Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Debugger-to-Execute-Malicious-Expression

## Summary

Set a breakpoint and start a backtest to force evaluation of the watched expression, displaying the XSS payload in the debugger UI.

## Description

With the malicious class in place, interacting with the debugger causes the backend to evaluate the overridden expression via WebSocket. The response is rendered unsanitized in the frontend, executing JS on the viewer's browser. This procedure targets both self-testing and victim triggering.

## Requirements

1. Malicious class already injected
2. Breakpoint set in algorithm code
3. Backtest initiation capability

## Defense

Defensive measures and detection strategies:

- Sanitize debugger display outputs
- Audit backtest requests for malicious code
- Implement JS execution policies in UI

## Objectives

1. Evaluate and render the payload
2. Confirm XSS in target browser
3. Simulate victim interaction

## Instructions

### Step 1: Set Breakpoint

**Context**: Pause execution to open debugger.

Add a breakpoint (e.g., import pdb; pdb.set_trace()) in the algorithm.

**Expected Output**: Debugger panel opens on backtest start.

### Step 2: Initiate Backtest

**Context**: Trigger the set_watch evaluation.

Click 'Start Backtest'; this sends [[commands/set-watch-websocket-message]] automatically.

> The message {"e":"set_watch","p":["get_datetime().strftime(\"%Y-%m-%d %H:%M:%S\")#__QUANTOPIAN__"]} evaluates the override.

**Expected Output**: Payload appears in date area, firing JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/set-watch-websocket-message]]

## Tools Used


## Tags

- debugger-trigger
- backtest-execution
