---
tags:
  - permission-bypass
  - bd-j
  - ps4
  - ps5
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9c76e687-231b-4352-af28-7bc9a6412bd2
created_at: '2025-12-11T03:47:57.383Z'
updated_at: '2025-12-11T03:47:57.383Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Bypass Permission Checks for File System Access

## Summary

This procedure bypasses permission checks to access and leak the file system on PS4 and PS5 via BD-J.

## Description

Using com.sony.gemstack.org.dvb.io.ixc.IxcProxy.invokeMethod, methods are called under privileged context by subclassing and implementing RemoteException-throwing interfaces.

## Requirements

1. Access to subclass target classes
2. Privileged context from prior steps
3. Target directories like /app0/

## Defense

Defensive measures and detection strategies:

- Enforce strict permission checks
- Monitor file access in privileged modes

## Objectives

1. Leak file system structure
2. Dump restricted files
3. Escalate access

## Instructions

### Step 1: Subclass Target Classes

**Context**: Implement interfaces for bypass.

Subclass classes like File and add RemoteException.

> This allows invokeMethod to call under privilege.

### Step 2: Invoke Methods

**Context**: Bypass checks for operations like File.list().

Call the methods to access restricted areas.

> Expected: Successful listing and dumping.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #permission-bypass
- #bd-j
