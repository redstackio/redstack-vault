---
tags:
  - xss
  - stored-xss
  - javascript
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-domain-semicolon]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.664Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 69272d48-6390-41b3-a49d-a9d0a936df3b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-into-Demo-Domain

## Summary

This procedure injects a modified javascript: payload into the Demo Domain field, appending a semicolon to evade duplicate checks from the Custom Domain injection, enabling a second stored XSS vector.

## Description

Similar to the Custom Domain, the Demo Domain field lacks sanitization for javascript: inputs. Federalist may check for duplicates, but adding a semicolon differentiates the payload, allowing storage. This triggers on viewing published demo sites, expanding the attack surface for admin-targeted XSS.

## Requirements

1. Authenticated session with site settings access.
2. Custom Domain already injected (to test duplicate bypass).
3. Target site ID known.

## Defense

Defensive measures and detection strategies:

- Validate and normalize inputs to detect minor variations like added semicolons in payloads.
- Use strict allowlists for domain fields (e.g., only valid TLDs).
- Audit admin actions for repeated suspicious inputs.

## Objectives

1. Bypass duplicate detection for payload storage.
2. Store second XSS instance for broader triggering.
3. Facilitate execution in published sites context.

## Instructions

### Step 1: Locate Demo Domain Field

**Context**: Find the input in the same settings form.

On the settings page, identify the Demo Domain field.

> Expected output: Field available below Custom Domain.

### Step 2: Enter Modified XSS Payload

**Context**: Use variant to avoid rejection.

**Command** ([[commands/javascript-alert-domain-semicolon]]):
```javascript
javascript:alert(document.domain);
```

> Input this into Demo Domain. Expected output: Accepted despite similarity to Custom payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-domain-semicolon]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[JavaScript]]
- [[bypass]]
