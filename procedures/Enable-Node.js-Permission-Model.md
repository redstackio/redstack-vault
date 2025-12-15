---
tags:
  - nodejs
  - permission-model
  - setup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-enable-permissions]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:44.846Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1a169832-9762-4ace-b712-438b1adb0aad
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enable-Node.js-Permission-Model

## Summary

This procedure activates the experimental permission model in Node.js 20.x, which restricts the capabilities of running code, such as disallowing native addons by default. It sets up a sandboxed environment intended to limit potential damage from untrusted scripts, but vulnerable to OpenSSL engine bypasses.

## Description

The Node.js permission model is an experimental feature designed to enhance security by enforcing granular permissions on file system access, network operations, and native module loading. Enabling it via the --experimental-permission flag simulates a secure runtime where malicious code should be contained. However, as discovered in vulnerability report #1954535, this model fails to restrict OpenSSL engine loading, allowing attackers to execute native code. This procedure is a prerequisite for demonstrating the bypass in a controlled setting. Prerequisites include Node.js 20.x installed and a basic JavaScript script to execute.

## Requirements

1. Node.js version 20.x or later installed on the target system.
2. Command-line access to run Node.js with flags.
3. A simple JavaScript file (e.g., script.js) to test the environment.

## Defense

Defensive measures and detection strategies:

- Monitor Node.js startup flags for --experimental-permission usage in production environments.
- Implement runtime monitoring for permission model state changes via custom logging.
- Use containerization or VM isolation to limit impact even if permissions are enabled.

## Objectives

1. Activate the permission model to restrict native addons and other capabilities.
2. Verify the model is active without errors.
3. Prepare the environment for vulnerability testing.

## Instructions

### Step 1: Launch Node.js with Permission Model

**Context**: Start the Node.js runtime with the experimental permission flag to enable restrictions. This applies to the entire process, disallowing native addons by default.

**Command** ([[commands/node-enable-permissions]]):
```bash
node --experimental-permission script.js
```

> This command runs the specified JavaScript file under the permission model. Expected output includes standard Node.js startup logs, with any permission checks visible if the script attempts restricted operations. Success is indicated by no startup errors and confirmation of restrictions (e.g., attempting to load a native module fails).

### Step 2: Verify Permission Restrictions

**Context**: Test that the model is enforcing restrictions, such as blocking native addon loads, to confirm setup.

**Command** ([[commands/node-test-native-addon]]):
```javascript
const addon = require('some-native-addon'); // This should fail
```

> Run within the enabled session. Expected output: Permission denied error for native module load, verifying the model's effectiveness before bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-enable-permissions]]
- [[commands/node-test-native-addon]]

## Tools Used


## Tags

- nodejs
- permission-model
- setup
