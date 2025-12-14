---
tags:
  - rce
  - file-upload
  - pentaho
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:54.325Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 06fcc421-c814-4a36-bc84-02892f63e7b1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-and-Execute-Malicious-PRPT-Report-for-RCE

## Summary

This procedure uploads a crafted malicious PRPT report to the Pentaho BI Server and executes it, triggering embedded scripts to achieve remote code execution and potential full system compromise.

## Description

With administrative access, the Pentaho interface allows uploading PRPT files without validating embedded scripts. Execution via scheduling or direct run invokes the scripts (e.g., BeanShell for command execution), leading to RCE. This exploits the lack of sandboxing in the report engine.

## Requirements

1. Administrative access to Pentaho BI Server
2. Crafted malicious .prpt file
3. Network connectivity to the upload endpoint

## Defense

Defensive measures and detection strategies:

- Implement file upload validation to strip or block scripts
- Log and monitor report executions for anomalous behavior
- Use intrusion detection systems (IDS) to flag unexpected process spawns
- Regularly audit uploaded reports and server logs

## Objectives

1. Successfully upload the PRPT file to the server
2. Trigger report execution to run embedded code
3. Confirm RCE through observable effects like malware or data exfiltration

## Instructions

### Step 1: Access Upload Interface

**Context**: Navigate to the report management section post-login.

In the Pentaho dashboard, go to the 'Upload' or 'New Report' feature.

### Step 2: Upload and Run Report

**Context**: Submit the file and initiate execution to exploit.

Select the malicious .prpt file for upload. Once uploaded, schedule or execute the report immediately.

> Monitor server responses or logs for execution confirmation, such as command output or errors indicating script run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[file-upload]]
- [[pentaho]]
