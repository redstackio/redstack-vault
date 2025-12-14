---
tags:
  - persistence
  - directory-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:29:19.983Z'
sub_techniques: []
id: d2b33a3e-0358-480a-aa94-b3f5173bef22
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Create-Directory-Structure-for-OpenSSL-Config

## Summary

This procedure creates the necessary directory structure on the Windows system drive root to host a malicious OpenSSL configuration file targeted by Slack's client.

## Description

On Windows systems, the C:\ drive root is writable by standard users, allowing creation of C:\usr\local\ssl\ without admin rights. This sets up the path for placing openssl.cnf, exploiting Slack's hardcoded load attempt for code injection and privilege escalation.

## Requirements

1. Local authenticated user account on Windows
2. Write access to C:\ (default for non-admin users)
3. No special tools required; use built-in commands or Explorer

## Defense

Defensive measures and detection strategies:

- Restrict write access to system root directories via Group Policy
- Monitor directory creation events in sensitive paths with Windows Event Logs
- Use file integrity monitoring tools like Sysmon

## Objectives

1. Prepare filesystem for config placement
2. Ensure path matches Slack's hardcoded reference
3. Avoid detection during setup

## Instructions

### Step 1: Navigate to System Root

**Context**: Access the writable C:\ drive.

Open Command Prompt or PowerShell and cd to C:\.

### Step 2: Create Nested Directories

**Context**: Build the full path structure.

Execute mkdir usr, then cd usr, mkdir local, cd local, mkdir ssl. Verify with dir C:\usr\local\ssl.

### Step 3: Confirm Permissions

**Context**: Ensure the path is ready for file creation.

Attempt to create a test file in C:\usr\local\ssl\ and delete it to validate write access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Persistence]]
- [[directory-creation]]
