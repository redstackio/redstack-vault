---
id: ac-discourse-cmd-inj-rce-backup
tags:
  - command-injection
  - rce
  - discourse
  - backup
  - shell-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Malicious-Discourse-Backup]]'
  - '[[procedures/Restore-Malicious-Backup-and-Login]]'
  - '[[procedures/Trigger-Command-Injection-via-User-Export]]'
step_count: 3
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:07.565Z'
description: >-
  Multi-stage attack exploiting command injection in Discourse's ExportCsvFile
  job by injecting shell commands into an admin username via the backup and
  restore feature, leading to remote code execution on the server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# Command Injection RCE via Malicious Username in Discourse Backup Restore

Multi-stage attack chain demonstrating a complete attack workflow exploiting a command injection vulnerability in Discourse's user archive export feature.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malicious Backup] --> B[Restore and Setup] --> C[Trigger Export and RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Archive extraction tools (e.g., tar, unzip)
- Text editor for modifying files

### Target Environment

- Discourse instance running Ruby on Rails
- Admin access to the target Discourse web application
- Server-side Linux environment for shell command execution

### Initial Access Requirements

- Valid admin credentials for the Discourse instance
- Network access to the web interface (e.g., HTTP/HTTPS)
- No prior server access needed; exploits web features

## Detailed Attack Procedures

### Step 1: Prepare Malicious Backup
procedure: [[procedures/Prepare-Malicious-Discourse-Backup]]

**Objective**: Create a backup archive, extract it, inject a malicious username containing shell commands, and repackage it to bypass username validation.

**Instructions**: Log in as admin and generate a backup via the admin panel. Download and extract the archive, then modify a username in the user data files to include the payload like `test.txt;wget mrzioto.com`. Repackage the archive.

**Expected Output**: A tampered backup archive ready for upload.

**Success Indicators**:
- Backup downloaded and extracted successfully
- Username modified with injection payload
- Archive repackaged without errors

### Step 2: Restore Malicious Backup and Login
procedure: [[procedures/Restore-Malicious-Backup-and-Login]]

**Objective**: Upload and restore the malicious backup to apply the injected username to the database, then log in to the modified account.

**Instructions**: Use the admin panel to upload the tampered archive and initiate restore. After restoration, log in using the account's email to access it despite special characters in the username.

**Expected Output**: Database updated with the malicious username; successful login to the account.

**Success Indicators**:
- Restore process completes without errors
- Login succeeds via email
- Username reflects the injected payload in the system

### Step 3: Trigger Command Injection via User Export
procedure: [[procedures/Trigger-Command-Injection-via-User-Export]]

**Objective**: Initiate a user archive export that triggers the vulnerable gzip command, executing the injected shell payload for RCE.

**Instructions**: From the modified account, send a POST request to the export endpoint with entity_type=user and entity=user_archive. The server will process the export, interpolating the malicious username into the shell command.

**Expected Output**: Injected command executes, e.g., file created and remote file downloaded via wget.

**Success Indicators**:
- Export request sent successfully
- Server-side command execution confirmed (e.g., via wget callback or file presence)
- RCE achieved without direct server access

## Attack Chain Summary

### Key Achievements

1. Bypassed username validation using backup/restore to inject shell metacharacters
2. Achieved RCE as the application user through unsanitized command interpolation
3. Demonstrated arbitrary command execution, such as file creation and remote downloads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
