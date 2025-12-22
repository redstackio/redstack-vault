---
tags:
  - nextcloud
  - setup
  - sharing
type: procedure
tools:
  - '[[tools/curl]]'
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
updated_at: '2025-12-14T17:29:19.915Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c313cce5-08e2-45e3-b1a5-a69e6a963cc3
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Nextcloud-Create-and-Share-Folder

## Summary

This procedure sets up a test environment in Nextcloud by creating a folder and file, then sharing it with read and reshare permissions to simulate the initial legitimate sharing scenario exploited in the privilege escalation vulnerability.

## Description

In the context of the Nextcloud sharing vulnerability, an attacker first needs a legitimate share to exploit. As User0 (original owner), create a folder /test containing file.txt, then share /test with User1 using permissions 17 (binary 10001: read=1 + reshare=16). This establishes the baseline where User1 can read but not delete. The vulnerability arises later in resharing, but this step ensures the setup mimics real-world file collaboration.

## Requirements

1. Valid Nextcloud admin or user credentials for User0
2. Access to Nextcloud web UI or API for file creation and sharing
3. Target Nextcloud instance running on accessible host (e.g., http://172.17.0.1:8081)

## Defense

Defensive measures and detection strategies:

- Monitor share creation events in Nextcloud logs for unusual permission patterns
- Enforce strict permission auditing on shares to prevent baseline misconfigurations

## Objectives

1. Establish a shared resource owned by User0
2. Grant User1 read and reshare access without delete
3. Prepare for escalation testing

## Instructions

### Step 1: Create Folder and File

**Context**: Use Nextcloud web UI or file API to create /test folder and /test/file.txt as User0.

No specific command; perform via UI: Log in as User0, navigate to Files, create folder 'test', upload or create 'file.txt' inside.

> Expected: Folder and file visible in User0's file list.

### Step 2: Share Folder with User1

**Context**: Share /test to User1 with permissions 17 via web UI or API.

Via UI: Right-click /test, select Share, add User1, set permissions to Can view + Can reshare (no edit/delete).

> Expected: Share notification to User1; API response if using endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- nextcloud
- setup
