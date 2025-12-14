---
tags:
  - insecure-storage
  - sqlite
  - credential-access
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
  - '[[tools/SQLite]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/adb-pull-database]]'
  - '[[commands/sqlite3-query-credentials]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:39.788Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: daab46da-5e66-4479-b1cb-9b92110249c7
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-Credentials-from-Vine-WebView-Database

## Summary

This procedure accesses the Vine app's internal storage to pull and query the WebView SQLite database, revealing plain text third-party credentials for potential unauthorized access to linked services.

## Description

With the app installed and database populated, an attacker uses ADB to extract `/data/data/co.vine.android/databases/webview.db` from the device's sandboxed storage. The database lacks encryption, storing credentials plainly due to developer oversight. Querying with sqlite3 exposes entries in tables like `webviewCookies`, enabling credential theft. Prerequisites include ADB setup and device connection; outcomes include direct access to usernames/passwords, amplified by WebView's JavaScript and file access features.

## Requirements

1. Android device connected via USB with ADB authorized
2. Vine app installed and database populated from prior logins
3. sqlite3 tool installed on host machine

## Defense

Defensive measures and detection strategies:

- Encrypt sensitive app data using Android Keystore or SQLCipher
- Restrict ADB access via policy enforcement
- Audit app storage for plain text secrets during code reviews

## Objectives

1. Extract the unencrypted webview.db file
2. Query database tables to retrieve credential data
3. Identify and exfiltrate plain text usernames/passwords

## Instructions

### Step 1: Pull Database File

**Context**: Use ADB to copy the database from internal storage to the host machine for analysis.

**Command** ([[commands/adb-pull-database]]):
```bash
adb pull /data/data/co.vine.android/databases/webview.db .
```

> This transfers webview.db to the current directory. Expected output: File downloaded, e.g., "4480 KB/s (12345 bytes in 0.002s)".

### Step 2: Query for Credentials

**Context**: Open the database with sqlite3 and select relevant tables to view plain text credentials.

**Command** ([[commands/sqlite3-query-credentials]]):
```bash
sqlite3 webview.db "SELECT * FROM webviewCookies;"
```

> This dumps rows; look for columns like `name` (e.g., username) and `value` (e.g., password) in plain text. Expected output: Tabular data showing unencrypted secrets.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/adb-pull-database]]
- [[commands/sqlite3-query-credentials]]

## Tools Used

- [[tools/Android-Debug-Bridge]]
- [[tools/SQLite]]

## Tags

- [[insecure-storage]]
- [[tools/SQLite]]
- [[credential-access]]
