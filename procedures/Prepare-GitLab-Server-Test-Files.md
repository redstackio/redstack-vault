---
tags:
  - gitlab
  - preparation
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/echo]]'
  - '[[tools/sudo]]'
tactics:
  - '[[Initial Access]]'
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
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0a55891b-42ca-47dd-ada0-992309e6c947
created_at: '2025-12-11T06:10:15.443Z'
updated_at: '2025-12-11T06:10:15.443Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Prepare GitLab Server Test Files

## Summary

This procedure creates test files on the GitLab server with specific ownership to demonstrate file read vulnerabilities in exploitation scenarios.

## Description

In GitLab vulnerability testing, preparing files in /tmp with git or root ownership simulates real-world readable targets. This setup is crucial for verifying bypasses in APIs like NuGet and wiki attachments, where ownership affects readability.

## Requirements

1. Server access to execute commands as root or with sudo.
2. GitLab environment with git user.
3. Local dummy files for uploads.

## Defense

Defensive measures and detection strategies:

- Monitor file creation in /tmp via auditd.
- Restrict sudo usage for ownership changes.

## Objectives

1. Create readable test files.
2. Test permission bypasses.
3. Verify file existence for exploitation.

## Instructions

### Step 1: Create Git-Owned Test File

**Context**: Prepare a file owned by git to test standard ownership scenarios.

**Command** ([[commands/create-test-file-git-owned]]):
```bash
echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg
```

> Writes 'hello' to /tmp/ggg and changes ownership to git:git. Expected: File created and owned correctly.

### Step 2: Create Root-Owned Test File

**Context**: Prepare a root-owned file to test bypasses without git restrictions.

**Command** ([[commands/create-test-file-root-owned]]):
```bash
echo hello > /tmp/ggg; sudo chown root:root /tmp/ggg
```

> Writes 'hello' to /tmp/ggg and changes ownership to root:root. Expected: File created for wiki API testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/create-test-file-git-owned]]
- [[commands/create-test-file-root-owned]]

## Tools Used

- [[tools/echo]]
- [[tools/sudo]]

## Tags

- [[gitlab]]
- [[preparation]]
