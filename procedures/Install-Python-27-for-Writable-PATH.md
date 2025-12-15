---
id: proc-python-install-001
tags:
  - setup
  - environment
  - python
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:19.673Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Install-Python-27-for-Writable-PATH

## Summary

This procedure installs Python 2.7 on a Windows target to add a writable directory (C:\Python27) to the system PATH, setting the stage for DLL hijacking attacks by making untrusted paths available for DLL searches.

## Description

In the context of exploiting DLL search order vulnerabilities, installing Python 2.7 introduces C:\Python27 as a PATH entry. This directory is writable by authenticated users and precedes trusted paths in some applications' DLL loading sequences, allowing placement of malicious DLLs like tcmalloc.dll. Prerequisites include administrative installation rights initially, but the resulting directory remains writable post-install. Expected outcome: A vulnerable PATH configuration exploitable by low-privileged users.

## Requirements

1. Windows target machine (e.g., Windows 10)
2. Download access to Python 2.7 installer from python.org
3. Initial admin privileges for installation (subsequent exploitation requires only authenticated user)

## Defense

Defensive measures and detection strategies:

- Remove unnecessary PATH entries like old Python directories
- Use tools like AppLocker or WDAC to restrict DLL loading to signed binaries
- Monitor PATH modifications via event logs (Event ID 4697 for service installs, but extend to env changes)

## Objectives

1. Establish a writable, untrusted PATH directory for DLL placement
2. Ensure compatibility with target application (Acronis True Image)
3. Minimize detection by using legitimate software installation

## Instructions

### Step 1: Download Python 2.7 Installer

**Context**: Obtain the official installer to avoid suspicion.

Download the Windows x86 MSI installer for Python 2.7.18 from https://www.python.org/downloads/release/python-2718/.

### Step 2: Install Python 2.7

**Context**: Perform default installation to add C:\Python27 to PATH.

Run the installer as administrator, select 'Install for all users', and ensure 'Add Python to PATH' is checked. Default path: C:\Python27.

> Post-install, verify with `echo %PATH%` in CMD; C:\Python27 should appear.

### Step 3: Verify Writable Directory

**Context**: Confirm authenticated users can write to the new directory.

As a low-privileged user, attempt to create a test file in C:\Python27, e.g., `echo test > C:\Python27\test.txt`.

> Expected: File created successfully without elevation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- python
- path-modification
