---
tags:
  - class-instantiation
  - bd-j
  - ps4
  - ps5
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 3fc521cf-d448-47db-8287-47e82afc5c41
created_at: '2025-12-11T03:47:57.445Z'
updated_at: '2025-12-11T03:47:57.445Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Instantiate Arbitrary Restricted Classes

## Summary

This procedure uses privileged access to instantiate arbitrary restricted classes in the BD-J environment on PS4 and PS5.

## Description

By calling com.oracle.security.Service.newInstance with arbitrary class names and a custom ProviderAccessor, restrictions are bypassed to load classes like sun.*.

## Requirements

1. Privileged context from prior deserialization exploit
2. Custom ProviderAccessor implementation
3. Vulnerable BD-J runtime

## Defense

Defensive measures and detection strategies:

- Restrict Class.forName calls
- Audit class loading in privileged contexts

## Objectives

1. Load restricted classes
2. Gain unauthorized access
3. Escalate capabilities

## Instructions

### Step 1: Prepare Custom ProviderAccessor

**Context**: Bypass checks for Class.forName.

Implement a custom accessor to allow arbitrary names.

> This enables calling on restricted classes.

### Step 2: Call newInstance

**Context**: Instantiate the classes.

Use Service.newInstance to load and instantiate.

> Expected: Successful instantiation without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #class-instantiation
- #bd-j
