---
id: proc-120312-modify-parent
tags:
  - idor
  - parameter-tampering
  - web
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:25:23.344Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Modify Parent Parameter for IDOR

## Summary

This procedure tampers with the 'parent' parameter in the captured HTTP request for Veris venue creation, changing it to an unauthorized value to exploit the IDOR vulnerability and bypass access controls.

## Description

The Veris application fails to validate user permissions for the 'parent' parameter, allowing direct object references to any venue ID. By editing this parameter in the request body or query, an attacker can target restricted parents. This step requires the captured request from the previous procedure and assumes knowledge of target parent IDs (e.g., via prior enumeration).

## Requirements

1. Captured original HTTP request from venue creation
2. Knowledge of unauthorized parent venue IDs
3. HTTP editing tool or proxy repeater

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks for all object references
- Log and alert on anomalous parent ID usage outside user scope

## Objectives

1. Alter 'parent' to unauthorized ID
2. Preserve request integrity for submission
3. Enable privilege escalation via hierarchy manipulation

## Instructions

### Step 1: Identify and Edit Parameter

**Context**: Locate the 'parent' field in the request and replace its value.

In the request body (e.g., form-data or JSON), find 'parent=123' and change to 'parent=456' where 456 is an unauthorized ID.

**Expected Output**: Updated request body with new parent value.

### Step 2: Validate Request Structure

**Context**: Ensure modifications do not break the request format.

Check headers, method, and other parameters remain unchanged; test syntax if using JSON.

**Expected Output**: Syntactically valid modified request.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[parameter-tampering]]
- [[web]]
