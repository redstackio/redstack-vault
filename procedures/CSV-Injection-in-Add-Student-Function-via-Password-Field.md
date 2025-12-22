---
id: proc-khan-csv-password-injection
tags:
  - csv-injection
  - unfiltered-input
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:28.315Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# CSV-Injection-in-Add-Student-Function-via-Password-Field

## Summary

This procedure injects malicious formulas into the password field during student addition, as no filtering is applied, enabling direct CSV payload inclusion upon export.

## Description

The add student function lacks CSV-specific sanitization for passwords, allowing full formula injection. When teachers download the user data CSV, the payload is preserved, setting up for RCE or file access on open.

## Requirements

1. Khan Academy teacher credentials
2. Malicious payload strings prepared
3. Access to download user CSV

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs, especially passwords, for CSV contexts
- Apply the same escaping rules to all export fields
- Audit add functions for injection risks

## Objectives

1. Add student with injected password
2. Confirm payload in exported CSV
3. Enable subsequent exploitation

## Instructions

### Step 1: Add Student with Payload

**Context**: Use the teacher interface to insert unfiltered payload.

Via web form:

- Navigate to add student.
- Set password to: `;=2+5+cmd|' /C calc'!A0`
- Complete addition.

> Payload stored without alteration.

### Step 2: Download and Verify CSV

**Context**: Export user data to check injection.

Trigger CSV download.

> Inspect file: Password field contains raw formula.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[unfiltered-input]]
- [[password-injection]]
