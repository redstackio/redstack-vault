---
tags:
  - api
  - quarantine
  - escalation
  - verify
type: procedure
tools:
  - '[[tools/requests-python-library]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:51.588Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9649735d-eb0b-4e85-9711-0a4cdf6e8888
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger-Quarantine-Overwrite-via-REST-API-and-Verify

## Summary

This procedure uses the anti_ransomware_service.exe REST API to trigger the quarantine of the detected file, causing the SYSTEM overwrite via the symlink, followed by verification of the escalation.

## Description

A Python script sends a request to http://localhost:6109/alerts to move the blocked ransomware_sim.exe to quarantine. The service, running as SYSTEM, copies it to the symlinked path without validation, overwriting the target file. Verification involves checking the file contents or executing the overwritten binary to confirm SYSTEM access. This completes the privilege escalation chain.

## Requirements

1. Symlink created in quarantine
2. Ransomware detection active (blocked but not closed)
3. Python with requests library installed
4. Localhost access to port 6109

## Defense

Defensive measures and detection strategies:

- Validate paths and block symlink following in quarantine operations
- Monitor REST API calls to local services for anomalies
- Integrity check critical system files like dpnsvr.exe

## Objectives

1. Trigger quarantine to perform overwrite
2. Achieve arbitrary file write as SYSTEM
3. Verify escalation potential

## Instructions

### Step 1: Trigger Quarantine via API

**Context**: Use requests to POST to the API endpoint for the detected alert.

**Command** (Python script invocation):
```cmd
python trigger_quarantine.py
```

> The script (using requests) sends a POST to http://localhost:6109/alerts with alert ID for the ransomware_sim.exe, requesting quarantine. Expected: 200 OK response, file moved.

### Step 2: Verify Overwrite

**Context**: Check the target file for modification.

No command; use file explorer or fc /b to compare original and new dpnsvr.exe contents.

> Expected: Target file replaced with ransomware_sim.exe payload, enabling execution as SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/requests-python-library]]

## Tags

- api
- quarantine
- escalation
- verify
