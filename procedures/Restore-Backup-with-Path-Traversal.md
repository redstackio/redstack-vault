---
id: proc-004
tags:
  - path-traversal
  - deserialization
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:33.053Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Restore-Backup-with-Path-Traversal

## Summary

This procedure intercepts and modifies the restore request to exploit path traversal in the `tables[]` parameter, triggering deserialization of the malicious payload to write a webshell to the filesystem.

## Description

The restore-tables endpoint at `/owncloud/index.php/apps/ownbackup/restore-tables` lacks validation on `tables[]`, allowing traversal like `../../admin/files` to alter the deserialization context. Using Burp Suite, the POST request is captured and modified after selecting the backup and table. This executes the serialized `Swift_Transport_SendmailTransport` to write the webshell, leading to RCE.

## Requirements

1. Created malicious backup
2. Burp Suite configured as proxy
3. Browser proxy set to Burp

## Defense

Defensive measures and detection strategies:

- Sanitize and validate path parameters in restore endpoints
- Implement web application firewall (WAF) rules for traversal patterns
- Log and alert on anomalous restore requests

## Objectives

1. Traverse directories to control deserialization
2. Deploy webshell via untrusted data processing
3. Achieve file write in target location

## Instructions

### Step 1: Initiate Restore

**Context**: Start the restore process to generate the interceptable request.

No command; in OwnBackup, select backup, choose table, click Restore tables.

> Request sent and intercepted by Burp.

### Step 2: Modify Request with Path Traversal

**Context**: Alter the `tables[]` parameter using Burp Suite.

In Burp Repeater or Proxy, change `tables[]=oc_accounts` to `tables[]=../../admin/files` and forward the POST request.

> Response indicates successful restore; check filesystem for `/tmp/pwned.php`.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[path-traversal]]
- [[deserialization]]
- [[tools/Burp-Suite]]
