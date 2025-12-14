---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Achieve-Remote-Code-Execution-via-Gadget-Chain
tags:
  - rce
  - command-injection
  - gadget-chain
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:28.180Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Achieve-Remote-Code-Execution-via-Gadget-Chain

## Summary

This procedure triggers the custom gadget chain built from PHP Object Injection to execute arbitrary commands on the ExpressionEngine server, resulting in remote code execution.

## Description

Once the gadget chain is injected, triggering it deserializes the objects in a way that chains method calls to invoke PHP functions capable of command execution (e.g., system(), exec()). In ExpressionEngine, this exploits the control panel's processing of gadgets. The target is a PHP-based web application, and success leads to full server compromise. Prerequisites include a successfully built chain from prior steps.

## Requirements

1. Injected and built gadget chain from previous procedure
2. Knowledge of PHP gadget chains that lead to command execution (e.g., using __destruct or __wakeup methods)
3. Ability to observe server responses or logs for output

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all deserialized inputs
- Disable dangerous PHP functions (e.g., exec, system) via disable_functions in php.ini
- Implement runtime application self-protection (RASP) to detect gadget chain patterns
- Regularly audit and update ExpressionEngine to patched versions

## Objectives

1. Trigger the gadget chain execution
2. Execute arbitrary server commands
3. Confirm RCE with observable effects

## Instructions

### Step 1: Trigger Deserialization

**Context**: Submit or activate the gadget in the control panel to force deserialization.

No specific command; interact with the UI element that processes the custom gadget (e.g., save or apply configuration).

> Monitor the response for errors or success. Expected output: No PHP fatal errors, chain executes silently.

### Step 2: Execute Command via Chain

**Context**: Ensure the gadget chain is configured to run a test command, such as 'id' or 'whoami'.

No specific command; the chain itself embeds the command (e.g., via a property that calls system('id')).

> If output is captured in response, it appears there; otherwise, check server logs or side effects like file writes. Expected output: Command results, e.g., 'uid=33(www-data) gid=33(www-data)'.

### Step 3: Validate RCE

**Context**: Run a confirmatory command to ensure full control.

No specific command; extend the chain to a payload that creates a file or pings a controlled server.

> Verify via external means (e.g., file existence or network traffic). Expected output: Evidence of command success, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[command-injection]]
- [[gadget-chain]]
