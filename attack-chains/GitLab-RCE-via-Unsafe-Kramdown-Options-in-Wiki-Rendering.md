---
id: fd29c25b-85e2-4a0d-afb8-3fa5a513ca1f
name: GitLab RCE via Unsafe Kramdown Options in Wiki Rendering
type: attack_chain
description: Exploitation chain for remote code execution in GitLab through unsafe inline options in Kramdown when rendering Wiki pages with .rmd extensions
verified: false
submitted: true
step_count: 5
created_at: 2025-12-09T00:20:44.980Z
updated_at: 2025-12-09T00:20:44.980Z
procedures:
  - "[[Upload Payload Snippet in GitLab]]"
  - "[[Clone and Modify GitLab Wiki Repository]]"
  - "[[Add Malicious RMD File to Wiki]]"
  - "[[Trigger Wiki Page Rendering for RCE]]"
  - "[[Verify Exploitation and Execute Reverse Shell]]"
techniques:
  - "[[Exploit Public-Facing Application]]"
  - "[[Command-Line Interface]]"
tactics:
  - "[[Initial Access]]"
  - "[[Execution]]"
  - "[[Persistence]]"
tags:
  - rce
  - gitlab
  - kramdown
  - wiki
  - command-injection
platforms:
  - Web
  - Linux
  - Docker
tools: []
commands: []
complexity: medium
skill_level: advanced
impact_level: high
validated: true
mitre_tactics:
  - "[[TA0001]]"
  - "[[TA0002]]"
  - "[[TA0003]]"
mitre_techniques:
  - "[[T1190]]"
  - "[[T1059]]"
---

# GitLab RCE via Unsafe Kramdown Options in Wiki Rendering

Multi-stage attack chain demonstrating remote code execution in GitLab by exploiting unsafe inline options in the Kramdown markdown parser during Wiki page rendering. The attack leverages the github-markup gem and Kramdown to instantiate arbitrary Ruby classes, leading to code execution via gadgets like Redis driver loading or command injection in GetProcessMem.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Payload] --> B[Clone Wiki]
    B --> C[Add Malicious File]
    C --> D[Trigger Rendering]
    D --> E[Verify and Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
```

## Prerequisites & Requirements

### Required Tools

- #git
- #nc

### Target Environment

- GitLab server on Linux/Docker
- Required services: GitLab Wiki, Redis 6.0.10, PostgreSQL 12.5, Git 2.29.0, Puma, Nginx, Sidekiq 5.2.9
- Network access to GitLab instance

### Initial Access Requirements

- User account with Wiki push access
- Ability to create snippets and projects
- Network position to access GitLab web interface and clone repositories

## Detailed Attack Procedures

### Step 1: Upload Payload Snippet - [[Upload Payload Snippet in GitLab]]

**Procedure**: [[Upload Payload Snippet in GitLab]]

**Objective**: Upload a Ruby payload file via a GitLab snippet to make it available on the server for later loading.

**Expected Output**: Payload file uploaded with a path like /uploads/-/system/user/1/c4119c5b144037f708ead7295cea4dd0/payload.rb.

**Success Indicators**:
- Snippet created successfully
- File attachment confirmed in snippet description

### Step 2: Clone Wiki Repository - [[Clone and Modify GitLab Wiki Repository]]

**Procedure**: [[Clone and Modify GitLab Wiki Repository]]

**Objective**: Create a new project with a Wiki and clone its repository to prepare for adding malicious content.

First, clone the Wiki repository using #git-clone-wiki-repo:

```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

Create a default home page in the Wiki.

**Expected Output**: Repository cloned successfully.

**Success Indicators**:
- Local copy of Wiki repository available
- Default Wiki page created

### Step 3: Add Malicious RMD File

**Procedure**: [Add-Malicious-RMD-File-to-Wiki](../procedures/Add-Malicious-RMD-File-to-Wiki.md)

**Objective**: Add a .rmd file with inline Kramdown options to exploit the rendering pipeline.

Stage changes with [git-add-all-changes](../commands/git-add-all-changes.md):

```bash
git add -A .
```

Commit with [git-commit-changes](../commands/git-commit-changes.md):

```bash
git commit -m "page1.rmd"
```

Push with [git-push-changes](../commands/git-push-changes.md):

```bash
git push
```

**Expected Output**: Malicious file pushed to Wiki.

**Success Indicators**:
- Commit and push successful
- Page appears in Wiki

### Step 4: Trigger Rendering for RCE - [[Trigger Wiki Page Rendering for RCE]]

**Procedure**: [[Trigger Wiki Page Rendering for RCE]]

**Objective**: Load the malicious Wiki page to trigger Kramdown rendering and execute the payload.

Refresh the Wiki and load the page1 page.

**Expected Output**: Code execution on server.

**Success Indicators**:
- Errors in GitLab logs
- Payload effects visible (e.g., file in /tmp)

### Step 5: Verify and Execute Reverse Shell - [[Verify Exploitation and Execute Reverse Shell]]

**Procedure**: [[Verify Exploitation and Execute Reverse Shell]]

**Objective**: Confirm execution and establish a reverse shell for further access.

Verify with #cat-tmp-file:

```bash
cat /tmp/vakzz
```

For reverse shell, trigger with nc command in payload, then run #id-display-user, #hostname-display-alias, #ps-list-processes, and #exit-shell.

**Expected Output**: Shell access and command outputs.

**Success Indicators**:
- File content matches expected
- Reverse shell connects and commands execute

## Attack Chain Summary

### Key Achievements

1. Arbitrary Ruby code execution via Kramdown options
2. Command injection without file uploads
3. Reverse shell on GitLab server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: [TIMESTAMP]*
