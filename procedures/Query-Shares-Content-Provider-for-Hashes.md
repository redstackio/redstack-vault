---
tags:
  - android
  - content-provider
  - credential-access
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/query-content-provider-shares]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Credentials from Password Stores]]'
updated_at: '2025-12-14T17:24:40.098Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 7e41cd23-82a2-4759-b53e-565cf1578f28
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials from Password Stores]]'
---
# Query-Shares-Content-Provider-for-Hashes

## Summary

This procedure queries the exported 'content://org.nextcloud/shares' Content Provider via ADB shell to extract bcrypt password hashes and share tokens for password-protected Nextcloud shares, enabling offline cracking.

## Description

The Nextcloud app's FileContentProvider is exported (exported=true in AndroidManifest.xml), allowing unrestricted access to local SQLite data. The 'shares' table contains 'share_with' (bcrypt hashes) and 'token' fields, leaked without authentication. This bypasses server brute-force limits.

## Requirements

1. ADB shell access established
2. Nextcloud app authenticated with protected shares synced
3. No root required

## Defense

Defensive measures and detection strategies:

- Patch app to v3.0+ where provider is restricted
- Use app sandboxing and monitor Content Provider queries via logs
- Encrypt local app data

## Objectives

1. Retrieve password hashes for cracking
2. Obtain share tokens for access
3. Demonstrate inter-app data leakage

## Instructions

### Step 1: Enter ADB Shell

**Context**: Ensure shell is active from prior setup.

Use [[commands/open-adb-shell]] if not already in shell.

### Step 2: Query Shares Provider

**Context**: Dump sensitive share data.

**Command** ([[commands/query-content-provider-shares]]):
```bash
content query --uri content://org.nextcloud/shares
```

> Queries the provider; output is a table with columns like ID, share_with (hash), token. Hashes appear as bcrypt strings (e.g., $2y$10$...).

**Expected Output**: Rows of share entries exposing hashes and tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Credentials from Password Stores]] Credentials from Password Stores

### Sub-Techniques


## Commands Used

- [[commands/query-content-provider-shares]]

## Tools Used

- [[tools/Android-Debug-Bridge]]

## Tags

- [[content-provider]]
- [[credential-access]]
