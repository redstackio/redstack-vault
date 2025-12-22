---
id: proc-uuid-trigger-injection
tags:
  - command-injection
  - rce
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-trigger-execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T05:32:13.357Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Trigger-Command-Injection-via-Uploaded-File

## Summary

This procedure triggers the execution of an uploaded malicious file on the server, exploiting improper handling to inject and run arbitrary commands, achieving remote code execution.

## Description

Following the upload, the Navy system's feature for processing files (e.g., preview or batch execution) failed to sanitize inputs, allowing command injection from the script. This step requests execution, leading to RCE on the DoD server.

## Requirements

1. Malicious file successfully uploaded with known path
2. Endpoint or feature that processes uploaded files
3. Ability to send follow-up HTTP requests

## Defense

Defensive measures and detection strategies:

- Never execute uploaded files directly; use sandboxing
- Input sanitization and parameterized queries for file handling
- Monitor for unexpected command executions in logs (e.g., via SIEM)

## Objectives

1. Cause the server to execute the uploaded script
2. Inject and run arbitrary commands
3. Confirm RCE through output or side effects

## Instructions

### Step 1: Request File Processing

**Context**: Send a request to the system to process or execute the uploaded file, assuming a vulnerable endpoint like /process.

**Command** ([[commands/curl-trigger-execution]]):
```bash
curl -X POST https://target-navy-system.com/process?file=malicious.sh
```

> If vulnerable, this triggers execution; look for command output in the response.

### Step 2: Verify Execution

**Context**: Check for side effects, such as a file created by the injected command, via a follow-up request if possible.

**Command** ([[commands/curl-trigger-execution]]):
```bash
curl https://target-navy-system.com/check?path=/tmp/pwned.txt
```

> Successful RCE shows the output from the injected command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-execution]]

## Tools Used


## Tags

- [[command-injection]]
- [[rce]]
- [[Execution]]
