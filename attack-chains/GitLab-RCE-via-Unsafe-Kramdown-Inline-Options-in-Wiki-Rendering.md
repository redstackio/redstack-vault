---
id: 5678c603-b972-4856-b413-efe2bf61519a
name: GitLab RCE via Unsafe Kramdown Inline Options in Wiki Rendering
type: attack_chain
description: >-
  Exploitation of unsafe inline options in Kramdown for GitLab Wiki rendering,
  leading to arbitrary Ruby code execution via class instantiation and command
  injection.
verified: false
submitted: true
step_count: 5
created_at: '2025-12-11T06:10:13.227Z'
updated_at: '2025-12-11T06:10:13.227Z'
procedures:
  - '[[procedures/Upload-Ruby-Payload-via-GitLab-Snippet]]'
  - '[[procedures/Create-and-Initialize-GitLab-Project-Wiki]]'
  - '[[procedures/Clone-Wiki-Repository-and-Add-Malicious-RMD-File]]'
  - '[[procedures/Push-Changes-and-Trigger-Wiki-Rendering]]'
  - '[[procedures/Verify-Payload-Execution-and-RCE]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Exploitation for Client Execution]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Persistence]]'
tags:
  - rce
  - gitlab
  - kramdown
  - ruby
  - command-injection
platforms:
  - Web
  - Linux
tools:
  - '[[tools/git]]'
  - '[[tools/Kramdown]]'
  - '[[tools/Rouge]]'
  - '[[tools/Redis-rb]]'
  - '[[tools/GetProcessMem]]'
  - '[[tools/GitHub::Markup]]'
  - '[[tools/nc]]'
commands:
  - '[[commands/ruby-puts-hello]]'
  - '[[commands/ruby-echo-tmp-file]]'
  - '[[commands/git-clone-wiki-repo]]'
  - '[[commands/git-add-all]]'
  - '[[commands/git-commit-message]]'
  - '[[commands/git-push]]'
  - '[[commands/cat-tmp-vakzz]]'
  - '[[commands/ps-memory-injection]]'
  - '[[commands/ruby-echo-inject-tmp]]'
  - '[[commands/id]]'
  - '[[commands/hostname-a]]'
  - '[[commands/ps-auxww]]'
  - '[[commands/exit]]'
  - '[[commands/nc-reverse-shell]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1059]]'
  - '[[T1203]]'
---

# GitLab RCE via Unsafe Kramdown Inline Options in Wiki Rendering

Multi-stage attack chain demonstrating exploitation of unsafe inline Kramdown options in GitLab Wiki rendering, allowing arbitrary Ruby class instantiation and code execution via uploaded payloads or direct command injection.

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
    A[Initial Access via Snippet Upload] --> B[Wiki Creation]
    B --> C[Malicious File Addition]
    C --> D[Trigger Rendering]
    D --> E[Verify Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
```

## Prerequisites & Requirements

### Required Tools

- [[tools/git]]
- [[tools/Kramdown]]
- [[tools/Rouge]]
- [[tools/Redis-rb]]
- [[tools/GetProcessMem]]
- [[tools/nc]]

### Target Environment

- GitLab 13.9.1-ee on Linux
- Required services/ports: GitLab UI (8080), Redis (9100), etc.
- Network access requirements: Access to GitLab instance with wiki push permissions

### Initial Access Requirements

- Credential requirements: GitLab user account with snippet creation and wiki push access
- Network position: External access to GitLab web interface
- Prior access needed: None beyond user account

## Detailed Attack Procedures

### Step 1: Upload Payload - [[procedures/Upload-Ruby-Payload-via-GitLab-Snippet]]

**Procedure**: [[procedures/Upload-Ruby-Payload-via-GitLab-Snippet]]

**Objective**: Upload a malicious Ruby payload to a predictable path on the GitLab server.

**Expected Output**: Payload file uploaded to /uploads/-/system/user/.../payload.rb.

**Success Indicators**:
- Snippet created successfully
- File attachment visible in snippet description

First, create a new snippet using GitLab UI and attach the Ruby payload containing [[commands/ruby-puts-hello]] and [[commands/ruby-echo-tmp-file]]:

```ruby
puts "hello from ruby"
`echo vakzz was here > /tmp/vakzz`
```

Note the upload path for later use.

### Step 2: Create Wiki - [[procedures/Create-and-Initialize-GitLab-Project-Wiki]]

**Procedure**: [[procedures/Create-and-Initialize-GitLab-Project-Wiki]]

**Objective**: Set up a new project and initialize its wiki for payload triggering.

**Expected Output**: Wiki repository created and cloned.

**Success Indicators**:
- New project visible in GitLab
- Default wiki home page created

Create a new project in GitLab UI, then initialize the wiki with a default page. Obtain the clone command.

### Step 3: Add Malicious File - [[procedures/Clone-Wiki-Repository-and-Add-Malicious-RMD-File]]

**Procedure**: [[procedures/Clone-Wiki-Repository-and-Add-Malicious-RMD-File]]

**Objective**: Clone the wiki repo and add a .rmd file with malicious Kramdown options referencing the payload.

**Expected Output**: Malicious page1.rmd added to repo.

**Success Indicators**:
- Repo cloned successfully
- File staged for commit

Clone the repo using [[commands/git-clone-wiki-repo]]:

```bash
git clone git@gitlab-docker.local:root/proj1.wiki.git
```

Add the .rmd file with syntax_highlighter_opts exploiting [[tools/Rouge]] and [[tools/Redis-rb]].

### Step 4: Push and Trigger - [[procedures/Push-Changes-and-Trigger-Wiki-Rendering]]

**Procedure**: [[procedures/Push-Changes-and-Trigger-Wiki-Rendering]]

**Objective**: Commit and push changes, then load the wiki page to trigger rendering and execution.

**Expected Output**: Payload executed during rendering.

**Success Indicators**:
- Changes pushed without errors
- Wiki page loads with potential error in logs

Stage and commit using [[commands/git-add-all]] and [[commands/git-commit-message]]:

```bash
git add -A .
git commit -m "page1.rmd"
```

Then push with [[commands/git-push]]:

```bash
git push
```

Refresh and load page1 in GitLab UI to trigger.

### Step 5: Verify Execution - [[procedures/Verify-Payload-Execution-and-RCE]]

**Procedure**: [[procedures/Verify-Payload-Execution-and-RCE]]

**Objective**: Check logs and filesystem for evidence of code execution.

**Expected Output**: Files like /tmp/vakzz created.

**Success Indicators**:
- Log entries showing execution
- File content verifiable via [[commands/cat-tmp-vakzz]]

Check /tmp with [[commands/cat-tmp-vakzz]]:

```bash
cat /tmp/vakzz
```

For command injection variant, use [[commands/ps-memory-injection]] or [[commands/ruby-echo-inject-tmp]].

## Attack Chain Summary

### Key Achievements

1. Arbitrary Ruby code execution on GitLab server
2. Potential compromise of entire instance
3. Demonstration of chained vulnerabilities in rendering pipeline

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Persistence]]

---

*Last updated: [TIMESTAMP]*
