---
tags:
  - rce
  - file-upload
  - gitlab
type: procedure
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/GitLab-Workhorse]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/perl-qx-execute-shell]]'
  - '[[commands/echo-write-file]]'
  - '[[commands/ruby-reverse-shell]]'
  - '[[commands/id-user-info]]'
  - '[[commands/hostname-alias]]'
  - '[[commands/ps-process-list]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d95cddc7-033a-41bc-8894-1b9ee0abce2e
created_at: '2025-12-11T06:10:22.450Z'
updated_at: '2025-12-11T06:10:22.450Z'
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
# Create GitLab Snippet and Upload Malicious File

## Summary

This procedure creates a new snippet in GitLab and uploads a crafted DjVu file disguised as JPG to trigger remote code execution via ExifTool's insecure handling of metadata.

## Description

By attaching the file in a snippet's description, GitLab Workhorse passes it to ExifTool based on extension, but ExifTool processes by content, executing embedded Perl code that injects commands like writing files to the server.

## Requirements

1. Valid GitLab account with snippet creation permissions
2. Crafted file (echo_vakzz.jpg) prepared
3. Access to GitLab web interface

## Defense

Defensive measures and detection strategies:

- Implement strict content-type validation in file uploads
- Monitor server logs for unexpected ExifTool executions or file creations in /tmp

## Objectives

1. Trigger RCE on GitLab server
2. Execute arbitrary commands as git user
3. Verify exploitation through file creation

## Instructions

### Step 1: Create New Snippet

**Context**: Navigate to the snippet creation page.

Go to https://gitlab.com/-/snippets/new and initiate a new snippet.

> Sets up the upload context.

### Step 2: Attach File in Description

**Context**: Select the file attachment option.

In the description field, click 'Attach a file'.

> Prepares for upload.

### Step 3: Upload Crafted File

**Context**: Upload the file to trigger the vulnerability.

Select and upload echo_vakzz.jpg, which executes [[commands/perl-qx-execute-shell]] embedding [[commands/echo-write-file]].

```bash
qx{echo vakzz >/tmp/vakzz}
```

> Leads to file /tmp/vakzz creation on server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/perl-qx-execute-shell]]
- [[commands/echo-write-file]]

## Tools Used

- [[tools/GitLab-Workhorse]]
- [[tools/ExifTool]]

## Tags

- rce
- file-upload
