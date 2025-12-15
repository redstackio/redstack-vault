---
tags:
  - rce
  - command-injection
  - node-js
  - git
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/git]]'
  - '[[tools/commit-msg]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-commit-msg-Module]]'
  - '[[procedures/Initialize-Git-Repository]]'
  - '[[procedures/Exploit-RCE-with-Malicious-Commit-Input]]'
  - '[[procedures/Verify-Exploitation-with-PoC-Script]]'
step_count: 4
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:19.363Z'
description: >-
  A multi-stage attack exploiting a remote code execution vulnerability in the
  commit-msg Node.js module (v0.2.3) through unsanitized user input in shell
  commands, allowing arbitrary command execution during Git commit validation.
skill_level: intermediate
impact_level: high
id: c791253d-530a-4a65-b1e4-5a49af165970
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# RCE in commit-msg Node.js Module via Malicious Commit Message Injection

Multi-stage attack chain demonstrating exploitation of an RCE vulnerability in the commit-msg Node.js module version 0.2.3, where user-supplied commit messages are directly concatenated into shell commands without sanitization, enabling arbitrary command execution on the developer's machine during Git commit validation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Vulnerable Module] --> B[Initialize Git Repo]
    B --> C[Inject Malicious Payload]
    C --> D[Execute PoC for Verification]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/git]]
- [[tools/commit-msg]]
- [[tools/node]]

### Target Environment

- Linux OS
- Node.js runtime installed
- npm package manager available
- Git version control system

### Initial Access Requirements

- Local access to a development machine with Node.js and Git installed
- No network access required; exploitation occurs locally during Git operations
- Prior installation of vulnerable dependencies not needed, as the attack installs the module

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-commit-msg-Module]]

**Objective**: Install the vulnerable commit-msg module globally to set up the exploitation environment.

**Instructions**: Use [[commands/npm-install-commit-msg]] to install the specific vulnerable version.

```bash
npm i commit-msg@0.2.3 -g
```

**Expected Output**: npm installation logs confirming successful global installation of commit-msg v0.2.3.

**Success Indicators**:
- Module installed and accessible via command line
- Version confirmed as 0.2.3 using `commit-msg --version`

### Step 2: Initialize Git Repository
procedure: [[procedures/Initialize-Git-Repository]]

**Objective**: Create a Git repository to enable the use of commit-msg for validation.

**Instructions**: Execute [[commands/git-init]] in the current directory to initialize a new repo.

```bash
git init
```

**Expected Output**: Message indicating "Initialized empty Git repository in /path/to/dir/.git/".

**Success Indicators**:
- .git directory created
- Git status shows empty repository ready for commits

### Step 3: Exploit RCE with Malicious Input
procedure: [[procedures/Exploit-RCE-with-Malicious-Commit-Input]]

**Objective**: Inject a malicious payload into the commit message to trigger arbitrary command execution via unsanitized shell formatting.

**Instructions**: Pipe a crafted payload using [[commands/echo-malicious-payload]] to commit-msg stdin.

```bash
echo "test||reboot" | commit-msg stdin
```

**Expected Output**: The injected command (e.g., reboot) executes, potentially rebooting the system or performing other actions.

**Success Indicators**:
- Arbitrary command runs (e.g., system reboot or file creation)
- No validation errors from commit-msg; shell command executes payload

### Step 4: Verify Exploitation
procedure: [[procedures/Verify-Exploitation-with-PoC-Script]]

**Objective**: Confirm RCE success by running a proof-of-concept script that checks for post-exploitation effects like file creation.

**Instructions**: Assume poc.js exists (create if needed with Node.js code to test file ops); execute using [[commands/node-run-poc]].

```bash
node poc.js
```

**Expected Output**: Script output indicating successful file creation (e.g., 'HACKED' file exists) or other RCE effects.

**Success Indicators**:
- Verification file or marker created
- Console logs confirm command execution from prior step

## Attack Chain Summary

### Key Achievements

1. Successful installation of vulnerable module without detection
2. Environment setup for Git commit validation
3. Arbitrary command execution via injected payload
4. Verification of full system compromise potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
