---
tags:
  - nodejs
  - openssl
  - bypass
  - rce
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/crypto-setEngine]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.843Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 142da0c6-4ef5-4de5-afbd-b254164b9200
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Load-Arbitrary-OpenSSL-Engine-via-crypto.setEngine

## Summary

This procedure exploits a gap in Node.js 20's permission model by using the crypto.setEngine() function to load an arbitrary OpenSSL engine, executing native code despite restrictions on native addons. It allows attackers to introduce malicious native functionality into the runtime.

## Description

The Node.js crypto module interfaces with OpenSSL for cryptographic operations and provides setEngine() to specify custom engines. In environments with the permission model enabled, native addons are blocked, but OpenSSL engine loading remains unrestricted due to an oversight in the permission implementation. By providing a path to a custom engine (a shared library like .so with a bind_fn implementing native code), attackers can execute arbitrary C/C++ code. This procedure assumes the permission model is active and requires a pre-compiled malicious engine. The attack scenario targets Node.js applications enforcing permissions, such as serverless functions or sandboxed scripts.

## Requirements

1. Node.js 20.x with permission model enabled.
2. A compatible OpenSSL engine library (e.g., custom .so file with bind_fn for native execution).
3. JavaScript script access within the Node.js environment.

## Defense

Defensive measures and detection strategies:

- Disable or restrict crypto.setEngine() usage via code reviews or wrappers in application code.
- Monitor for OpenSSL engine loads in Node.js logs or via runtime hooks.
- Update to patched Node.js versions addressing this vulnerability (post-report fixes).

## Objectives

1. Load a malicious OpenSSL engine without permission denials.
2. Confirm the engine is active for crypto operations.
3. Set up for native code execution in the next stage.

## Instructions

### Step 1: Import Crypto Module and Set Engine

**Context**: Within the JavaScript script running under permissions, require the crypto module and call setEngine with the engine identifier and function.

**Command** ([[commands/crypto-setEngine]]):
```javascript
const crypto = require('crypto');
crypto.setEngine('path/to/malicious_engine', 'bind_fn');
```

> This loads the specified engine, executing its initialization native code. Expected output: No errors; subsequent crypto calls use the engine. Verify by checking if crypto operations succeed without standard restrictions.

### Step 2: Trigger Engine Initialization

**Context**: Perform a basic crypto operation to invoke the engine's bind_fn, ensuring native code loads.

**Command** ([[commands/crypto-trigger-operation]]):
```javascript
const hash = crypto.createHash('sha256').update('test').digest();
console.log(hash.toString('hex'));
```

> Expected output: Hash value computed via the custom engine, with any native side effects (e.g., logs from bind_fn) indicating successful load.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/crypto-setEngine]]
- [[commands/crypto-trigger-operation]]

## Tools Used


## Tags

- nodejs
- openssl
- bypass
- rce
