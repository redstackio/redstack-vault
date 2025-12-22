---
id: proc-identify-bypass
tags:
  - bypass
  - escaping
  - structured-clone
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/define-escaping-function]]'
  - '[[commands/test-normal-escaping]]'
  - '[[commands/test-error-bypass]]'
  - '[[commands/create-file-object]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.421Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Identify-Escaping-Function-Bypass

## Summary

This procedure analyzes and tests the HTML escaping function in the Shopify dialog code to identify bypasses using objects without hasOwnProperty for certain properties, such as Error and File, which are cloneable via postMessage.

## Description

The escaping function u iterates over object properties using for...in and only escapes if hasOwnProperty returns true, skipping non-enumerable properties like 'name' on File objects. This allows injecting malicious HTML that survives cloning and reaches DOM insertion unescaped.

## Requirements

1. Browser console on a page able to execute JS
2. Knowledge of JS object prototypes and enumeration
3. Access to Ve.escapeHtml (assume DOMPurify or similar)

## Defense

Defensive measures and detection strategies:

- Escape all properties recursively, including non-enumerable ones.
- Avoid structured clones for untrusted data; use JSON.parse/stringify instead.
- Sanitize inputs before DOM insertion with comprehensive libraries.

## Objectives

1. Confirm escaping skips non-enumerable properties.
2. Validate File objects as viable for bypass.
3. Demonstrate unescaped payload survival.

## Instructions

### Step 1: Define Escaping Function

**Context**: Replicate the vulnerable u function in console.

**Command** ([[commands/define-escaping-function]]):
```javascript
function u(payload){for(var idx in payload){if(payload.hasOwnProperty(idx)){ payload[idx]= Ve.escapeHtml(payload[idx]);}} return payload;}
```

> Assumes Ve.escapeHtml exists; test with mock if needed.

### Step 2: Test Normal String Escaping

**Context**: Verify function works on plain objects.

**Command** ([[commands/test-normal-escaping]]):
```javascript
result =u({message:"'\"<b>"}); result.message
```

> Outputs escaped: &#39;&quot;&lt;b&gt;

### Step 3: Test Error Object Bypass

**Context**: Use Error, which has non-enumerable message.

**Command** ([[commands/test-error-bypass]]):
```javascript
result =u(new Error("'\"<b>")); result.message;
```

> message remains unescaped: ' "<b>

### Step 4: Test File Object

**Context**: Create File and check 'name' property.

**Command** ([[commands/create-file-object]]):
```javascript
let f =new File(["data"],"controlledvalue"); f.name; f.hasOwnProperty("name");
```

> name: controlledvalue; hasOwnProperty: false

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/define-escaping-function]]
- [[commands/test-normal-escaping]]
- [[commands/test-error-bypass]]
- [[commands/create-file-object]]

## Tools Used


## Tags

- bypass
- escaping
