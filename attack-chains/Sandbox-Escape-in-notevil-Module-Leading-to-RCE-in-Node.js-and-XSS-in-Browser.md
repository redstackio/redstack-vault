---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Sandbox Escape in notevil Module Leading to RCE in Node.js and XSS in Browser
type: attack_chain
description: >-
  Multi-stage exploitation of a sandbox escape vulnerability in the notevil
  Node.js module, enabling arbitrary JavaScript execution for remote code
  execution (RCE) on the server or cross-site scripting (XSS) in the browser via
  dependent packages like react-schema-form.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.410Z'
procedures:
  - '[[procedures/Load-notevil-Module-for-SafeEval]]'
  - '[[procedures/Craft-Malicious-JavaScript-for-Sandbox-Escape]]'
  - '[[procedures/Execute-Sandbox-Escape-Payload-in-Node.js]]'
  - '[[procedures/Exploit-XSS-in-react-schema-form]]'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
tags:
  - sandbox-escape
  - rce
  - xss
  - nodejs
  - javascript
platforms:
  - Node.js
  - Web
tools:
  - '[[tools/notevil]]'
  - '[[tools/esprima]]'
  - '[[tools/runkit]]'
  - '[[tools/react-schema-form]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---

# Sandbox Escape in notevil Module Leading to RCE in Node.js and XSS in Browser

Multi-stage attack chain demonstrating exploitation of the notevil module's sandbox escape vulnerability (version 1.3.2), allowing bypass of AST-based restrictions to access global objects, load Node.js modules for RCE, or inject scripts for XSS in browser contexts like react-schema-form.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Load notevil Module] --> B[Craft Malicious Payload]
    B --> C[Execute in Node.js for RCE]
    C --> D[Adapt for Browser XSS]
    D --> E[Arbitrary Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/notevil]]
- [[tools/runkit]]
- [[tools/react-schema-form]]

### Target Environment

- Node.js runtime (version compatible with notevil 1.3.2)
- Browser environment for XSS (e.g., react-schema-form demo)
- npm for package installation

### Initial Access Requirements

- Access to a Node.js environment or browser demo page
- No specific credentials required; assumes developer or testing context
- Network access to npm registry and demo sites

## Detailed Attack Procedures

### Step 1: Load notevil Module

procedure: [[procedures/Load-notevil-Module-for-SafeEval]]

**Objective**: Import the vulnerable notevil module to obtain the safeEval function for restricted JavaScript evaluation.

**Instructions**: Install and require the notevil module using npm in a Node.js script.

**Expected Output**: safeEval function loaded successfully.

**Success Indicators**:
- Module requires without errors
- safeEval function is available for use

### Step 2: Craft Malicious JavaScript

procedure: [[procedures/Craft-Malicious-JavaScript-for-Sandbox-Escape]]

**Objective**: Construct a JavaScript payload that bypasses the sandbox by manipulating function prototypes to access and bind the Function constructor.

**Instructions**: Define the code string that uses Object.getOwnPropertyDescriptors on fn.__proto__.constructor to extract and rebind properties, enabling execution of arbitrary code like loading the 'util' module.

**Expected Output**: Valid JavaScript string ready for evaluation.

**Success Indicators**:
- Payload string is syntactically correct
- No parsing errors when inspected

### Step 3: Execute in Node.js for RCE

procedure: [[procedures/Execute-Sandbox-Escape-Payload-in-Node.js]]

**Objective**: Evaluate the crafted payload using safeEval to escape the sandbox and achieve RCE, such as logging via the util module.

**Instructions**: Pass the payload to safeEval and log the result in a Node.js console.

**Expected Output**: 'pwned' logged to console, indicating successful module load and execution outside the sandbox.

**Success Indicators**:
- Console output shows 'pwned'
- No sandbox restrictions prevent global access

### Step 4: Exploit XSS in Browser

procedure: [[procedures/Exploit-XSS-in-react-schema-form]]

**Objective**: Adapt the payload for browser execution in react-schema-form, injecting it into form conditions to trigger XSS.

**Instructions**: Configure the form JSON with the malicious condition and schema requiring the field, then submit to render and execute the alert.

**Expected Output**: Alert popup displaying 'pwned ' in the browser.

**Success Indicators**:
- Form renders without errors
- Alert executes on submission

## Attack Chain Summary

### Key Achievements

1. Bypassed notevil's AST-based sandbox restrictions using prototype manipulation.
2. Achieved RCE in Node.js by loading and executing modules like util.
3. Demonstrated XSS in browser-dependent packages via user-controlled form fields.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]] JavaScript
- [[Drive-by Compromise]] Drive-by Compromise

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
