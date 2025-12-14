---
id: p3b2c3d4-e5f6-7890-abcd-ef1234567893
name: Trigger-Elevated-Execution-via-Software-Installation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.867Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Bypass User Account Control]]'
sub_techniques: []
tags:
  - uac-bypass
  - installation-hijack
  - rce
commands: []
platforms:
  - Windows
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---

# Trigger-Elevated-Execution-via-Software-Installation

## Summary

This procedure triggers the Malstaller payload by inducing an administrator to run an elevated software installation, uninstallation, or native tool that invokes a URL, causing the hijacked HKCU handler to execute the malicious batch script with UAC-elevated privileges.

## Description

Installers from popular software and Windows natives (e.g., mmc.exe) often open URLs like privacy policies during elevated runs. Since they query HKCU for the default handler without sanitization, the tampered keys redirect to malstaller.bat, which runs as admin. This bypasses typical UAC prompts and enables RCE, affecting tools like perfmon.exe across Windows versions.

## Requirements

1. Pre-setup registry tampering and batch script
2. Admin user to perform the elevated action
3. Target software that triggers URL opens (e.g., any installer with links)

## Defense

Defensive measures and detection strategies:

- Audit installer behaviors; force HKLM usage for handlers
- Enable UAC secure desktop and log elevation events (Event ID 4624)
- Use endpoint detection to flag anomalous batch executions during installs

## Objectives

1. Achieve RCE in elevated context via trusted process
2. Log sensitive data (e.g., URLs) to confirm escalation
3. Exploit without additional user interaction beyond normal workflow

## Instructions

### Step 1: Select Trigger Mechanism

**Context**: Identify or prepare a software process that runs elevated and opens URLs.

**Instructions**: Choose an installer (e.g., download a benign app) or native tool like `perfmon.exe /run` that prompts for links.

> No command; manual selection. Expected: Process ready for elevation.

### Step 2: Initiate Elevated Process

**Context**: Run the software as administrator to invoke UAC.

**Instructions**: Right-click the installer or tool and select "Run as administrator". During execution, click any URL link (e.g., privacy policy).

> Triggers the handler. Expected: UAC prompt accepted, process continues.

### Step 3: Verify Execution

**Context**: Check for payload activation post-trigger.

**Instructions**: Examine C:\mal_log.txt for new entries and confirm browser opened.

> Success: Log shows date/URL, elevated write succeeded.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[uac-bypass]]
- [[installation-hijack]]
- [[rce]]
