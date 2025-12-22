---
tags:
  - xxe
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/post-upload-image]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[File and Directory Discovery]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 9c906dec-a41f-42af-aafc-2c5b87169db3
created_at: '2025-12-13T09:00:33.710Z'
updated_at: '2025-12-13T09:00:33.710Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Escalate XXE to File Exfiltration

## Summary

Escalate XXE to read and exfiltrate server files.

## Description

Craft DTD for file reading and use OOB channels like FTP simulation to receive contents.

## Requirements

1. Confirmed XXE
2. Custom DTD server

## Defense

- File system permissions
- Network egress filtering

## Objectives

1. Read sensitive files
2. Exfiltrate data

## Instructions

### Step 1: Upload Escalated Payload

**Context**: Trigger file read.

**Command** ([[commands/post-upload-image]]):
```bash
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: target.com
```

> With DTD for /etc/passwd exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques

## Commands Used

- [[commands/post-upload-image]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[xxe]]
- [[Exfiltration]]
