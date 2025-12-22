---
id: uuid-proc-4
name: Observe-HTML-Rendering-and-Local-File-Execution
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.545Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - xss
  - local-execution
  - file-protocol
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Observe-HTML-Rendering-and-Local-File-Execution

## Summary

This procedure observes the rendering of the injected HTML in the Nextcloud client's error alert box, confirming arbitrary local file execution without user confirmation due to the trusted context.

## Description

The alert box in the Nextcloud desktop client fails to sanitize HTML from error responses, interpreting tags and allowing file:// protocol links to execute local binaries on Windows. This step validates the full exploit chain, where clicking or auto-rendering the link launches files like calc.exe, bypassing typical security prompts in an elevated permission zone similar to legacy IE behaviors.

## Requirements

1. Malicious response already injected and forwarded
2. Alert box displayed in the client
3. Target Windows environment with accessible local files

## Defense

Defensive measures and detection strategies:

- Patch client to escape HTML in error displays
- Monitor for unexpected process launches (e.g., calc.exe) via EDR

## Objectives

1. Verify HTML interpretation in the alert box
2. Achieve local file execution
3. Confirm bypass of authorization prompts

## Instructions

### Step 1: View the Alert Box

**Context**: Inspect the displayed error message for HTML rendering.

The alert box shows the response body; observe if tags like <A> are clickable and functional.

> HTML is rendered as intended, with links active.

### Step 2: Trigger File Execution

**Context**: Interact with the payload to execute the local file.

Click the injected link (e.g., CALC.EXE) or note auto-execution if applicable.

> The target file (calc.exe) launches without confirmation dialogs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- local-execution
- file-protocol
