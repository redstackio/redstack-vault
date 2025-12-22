---
tags:
  - nodejs
  - openssl
  - privilege-escalation
  - rce
  - sandbox-bypass
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-Node.js-Permission-Model]]'
  - '[[procedures/Load-Arbitrary-OpenSSL-Engine-via-crypto.setEngine]]'
  - '[[procedures/Achieve-Arbitrary-Code-Execution-Bypassing-Permissions]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.848Z'
description: >-
  Multi-stage attack exploiting a vulnerability in Node.js 20's permission model
  by loading arbitrary OpenSSL engines to achieve code execution and privilege
  escalation.
skill_level: intermediate
impact_level: high
id: 08b3d755-ec42-424f-aa61-c43991b58ac0
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass Node.js Permission Model via Arbitrary OpenSSL Engine Loading

Multi-stage attack chain demonstrating exploitation of Node.js 20's permission model vulnerability, allowing arbitrary native code execution through OpenSSL engines.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable Permission Model] --> B[Load OpenSSL Engine]
    B --> C[Arbitrary Code Execution]
    C --> D[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Node.js 20.x environment
- Compatible OpenSSL engine (e.g., custom .so file implementing bind_fn for native code)

### Target Environment

- Node.js runtime version 20.x
- OpenSSL library integrated with Node.js
- Permission model enabled via --experimental-permission

### Initial Access Requirements

- Local or remote access to execute Node.js scripts
- Ability to run JavaScript code in the Node.js environment
- Pre-built OpenSSL engine library for loading

## Detailed Attack Procedures

### Step 1: Enable Permission Model
procedure: [[procedures/Enable-Node.js-Permission-Model]]

**Objective**: Activate Node.js's experimental permission model to restrict code capabilities, setting up the conditions for bypass demonstration.

**Instructions**: Launch Node.js with the permission model enabled using the appropriate flag. This step simulates a secured environment where native addons are disallowed by default.

```bash
node --experimental-permission script.js
```

**Expected Output**: Node.js starts with permission model active, logging any permission checks but allowing script execution under restrictions.

**Success Indicators**:
- Permission model enabled (verifiable via Node.js logs or internal checks)
- Native addons disallowed, confirming restrictions are in place

### Step 2: Load Arbitrary OpenSSL Engine
procedure: [[procedures/Load-Arbitrary-OpenSSL-Engine-via-crypto.setEngine]]

**Objective**: Use the crypto module to load a malicious OpenSSL engine, bypassing restrictions on native code execution.

**Instructions**: Within the JavaScript script, import the crypto module and invoke [[commands/crypto-setEngine]] with the path to a custom OpenSSL engine. The engine must be compatible and contain native code in its bind_fn.

```javascript
const crypto = require('crypto');
crypto.setEngine('path/to/malicious_engine', 'bind_fn');
```

**Expected Output**: The engine loads successfully without triggering permission denials, as the permission model does not restrict OpenSSL engine loading.

**Success Indicators**:
- No permission errors during engine load
- Crypto operations now use the loaded engine, confirming bypass initiation

### Step 3: Achieve Arbitrary Code Execution
procedure: [[procedures/Achieve-Arbitrary-Code-Execution-Bypassing-Permissions]]

**Objective**: Execute native code from the loaded engine to disable the permission model and escalate privileges for further JavaScript operations.

**Instructions**: Trigger cryptographic operations that invoke the engine's native code, such as generating a hash. The native code within the engine can modify Node.js internals (e.g., set Permission::enabled_ to false) to fully disable restrictions.

```javascript
const hash = crypto.createHash('sha256').update('data').digest();
console.log(hash);
```

**Expected Output**: Native code executes arbitrarily, potentially logging or performing actions like disabling permissions, followed by unrestricted JavaScript execution.

**Success Indicators**:
- Native code runs without permission blocks
- Permission model disabled, allowing escalated operations (e.g., file access or network calls previously restricted)

## Attack Chain Summary

### Key Achievements

1. Successfully enabled Node.js permission model to establish a controlled, restricted environment.
2. Bypassed native addon restrictions by loading an arbitrary OpenSSL engine via crypto.setEngine().
3. Achieved arbitrary native code execution, disabling the permission model for full privilege escalation.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
