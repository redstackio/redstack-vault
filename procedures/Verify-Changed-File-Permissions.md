---
id: p-verify-change
name: Verify-Changed-File-Permissions
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.777Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials In Files]]'
sub_techniques: []
tags:
  - verification
  - permissions
  - exposure
commands:
  - '[[commands/ls-check-final-permissions]]'
platforms:
  - Linux
tools:
  - '[[tools/ls]]'
skill_level: basic
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Verify-Changed-File-Permissions

## Summary

This procedure inspects the cookie jar file after the curl operation to confirm that permissions have been altered from secure (0600) to exposed (0644), validating the information disclosure vulnerability in libcurl.

## Description

Post-exploitation, the file's permissions are checked using ls to observe the change introduced by libcurl's cookie jar handling. This step confirms the impact: sensitive cookies now accessible to group and world users on the system. Applicable to Linux environments where the vulnerability exists. Expected outcome: Visible permission relaxation, indicating potential leak of confidential data like authentication tokens.

## Requirements

1. Linux with ls command.
2. cookie.jar file modified by prior curl execution.
3. Read access to the file and directory.

## Defense

Defensive measures and detection strategies:

- Implement permission auditing scripts to alert on changes to sensitive files.
- Use immutable file attributes (chattr +i) for critical credential stores.
- Regularly scan for world-readable files containing sensitive patterns (e.g., cookies).

## Objectives

1. Confirm permission overwrite success.
2. Quantify exposure risk.
3. Validate vulnerability exploitation.

## Instructions

### Step 1: Check Updated Permissions

**Context**: List the file details to see the new permissions after libcurl's write operation.

**Command** ([[commands/ls-check-final-permissions]]):
```bash
ls -l cookie.jar
```

> ls -l shows long format. Expected output: -rw-r--r-- 1 user group [size] [date] cookie.jar, indicating 0644 mode and exposure.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/ls-check-final-permissions]]

## Tools Used

- [[tools/ls]]

## Tags

- verification
- permissions
- exposure
