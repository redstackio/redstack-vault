---
id: p-create-secure-jar
name: Create-and-Verify-Secure-Cookie-Jar-File
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.788Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials In Files]]'
sub_techniques: []
tags:
  - setup
  - permissions
  - file-creation
commands:
  - '[[commands/install-create-cookie-jar]]'
  - '[[commands/ls-check-initial-permissions]]'
platforms:
  - Linux
tools:
  - '[[tools/install]]'
  - '[[tools/ls]]'
skill_level: basic
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---

# Create-and-Verify-Secure-Cookie-Jar-File

## Summary

This procedure creates an empty file intended as a cookie jar with strict owner-only permissions (0600) and verifies its initial state, simulating secure storage of sensitive authentication cookies before exploitation.

## Description

In a multi-user Linux environment, sensitive files like cookie jars should have permissions restricting access to the owner only. This step uses the install utility to create such a file from /dev/null (empty source) and ls to confirm the permissions. This setup is crucial for demonstrating the libcurl vulnerability where subsequent cookie saves overwrite these protections. The target is any Linux system with standard tools, assuming a default umask of 022. Expected outcome: a file ready for vulnerability testing without initial exposure.

## Requirements

1. Linux environment with install and ls commands available (standard on most distributions).
2. Write permissions in the current working directory.
3. No elevated privileges needed.

## Defense

Defensive measures and detection strategies:

- Use file monitoring tools like auditd to log permission changes on sensitive files.
- Enforce strict umask (e.g., 077) system-wide to prevent accidental exposures.

## Objectives

1. Establish a baseline secure file for testing credential storage.
2. Confirm no initial access by non-owners.
3. Prepare for vulnerability trigger without prior leaks.

## Instructions

### Step 1: Create the Secure Cookie Jar File

**Context**: This creates an empty file named cookie.jar with mode 0600 using install from /dev/null as source.

**Command** ([[commands/install-create-cookie-jar]]):
```bash
install -m 600 /dev/null cookie.jar
```

> The install command sets the file mode to rw------- (0600), copying empty content from /dev/null. Expected output: No stdout, file created successfully.

### Step 2: Verify Initial Permissions

**Context**: Inspect the file to ensure permissions are correctly set to owner-only access.

**Command** ([[commands/ls-check-initial-permissions]]):
```bash
ls -l cookie.jar
```

> ls -l displays long format details. Expected output: -rw------- 1 user group 0 [date] cookie.jar, confirming 0600 permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/install-create-cookie-jar]]
- [[commands/ls-check-initial-permissions]]

## Tools Used

- [[tools/install]]
- [[tools/ls]]

## Tags

- setup
- permissions
- file-creation
