---
tags:
  - windows
  - directory-creation
  - persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-directory-path]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:26:17.501Z'
sub_techniques: []
id: 4b49b56d-5ac9-4266-9519-008cad74780c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Create Insecure OpenSSL Directory Path

## Summary

This procedure creates the default OpenSSL directory structure on Windows if it doesn't exist, exploiting the fact that low-privileged users can write to C:\ root, setting up for config injection.

## Description

Due to mingw and Visual C build assumptions, paths like C:\usr\local\ssl are not secured. This step establishes the directory, allowing placement of malicious files. It's part of local privilege escalation chains targeting OpenSSL-dependent applications.

## Requirements

1. Low-privileged Windows user
2. Command prompt access
3. Writable C:\ root (default for standard users)

## Defense

Defensive measures and detection strategies:

- Restrict writes to C:\ with Group Policy or ACLs
- Audit directory creations in system roots
- Use AppLocker to block unauthorized mkdir in sensitive paths

## Objectives

1. Create writable OPENSSLDIR structure
2. Prepare environment for config tampering
3. Enable subsequent malicious file placement

## Instructions

### Step 1: Create Directory Tree

**Context**: Build the full path for OpenSSL config, such as C:\usr\local\ssl.

**Command** ([[commands/create-directory-path]]):
```cmd
mkdir C:\usr\local\ssl
```

> This creates the directory if absent. On success, no error; verify with dir.

### Step 2: Confirm Writability

**Context**: Test file creation in the new directory to ensure exploitability.

**Command** (built-in echo):
```cmd
echo test > C:\usr\local\ssl\test.txt
```

> If successful, delete the test file; confirms low-priv write access.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell

### Sub-Techniques


## Commands Used

- [[commands/create-directory-path]]

## Tools Used


## Tags

- [[windows]]
- [[directory-creation]]
