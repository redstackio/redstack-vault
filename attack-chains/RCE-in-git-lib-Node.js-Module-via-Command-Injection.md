---
id: ac-rce-git-lib-injection
tags:
  - rce
  - command-injection
  - node.js
  - git-lib
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/git]]'
  - '[[tools/Node.js]]'
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
  - '[[procedures/Exploit-git-lib-RCE-via-Command-Injection]]'
step_count: 6
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:19.808Z'
description: >-
  A multi-stage attack chain exploiting a command injection vulnerability in the
  git-lib Node.js module (v1.6.0) to achieve remote code execution by injecting
  shell commands into the git.add() function.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# RCE in git-lib Node.js Module via Command Injection

Multi-stage attack chain demonstrating exploitation of insecure command formatting in the git-lib Node.js module to execute arbitrary OS commands.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Prepare PoC]
    B --> C[Install Vulnerable Module]
    C --> D[Initialize Git Repo]
    D --> E[Execute Malicious PoC]
    E --> F[Verify RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/git]]
- [[tools/Node.js]]

### Target Environment

- Node.js runtime (v10+ recommended)
- Linux OS for shell command execution
- No specific services or ports required; local execution

### Initial Access Requirements

- Local access to a development machine or server running Node.js
- No network access or credentials needed; exploits local module usage

## Detailed Attack Procedures

### Step 1: Prepare Proof of Concept
procedure: [[procedures/Exploit-git-lib-RCE-via-Command-Injection]]

**Objective**: Create a JavaScript file that invokes the vulnerable git.add() function with a malicious payload to inject shell commands.

**Instructions**: Write a file named `poc.js` using Node.js that requires the git-lib module and calls `git.add('test;touch HACKED;')`. This injects a semicolon to chain the `touch HACKED` command after the legitimate git operation.

**Expected Output**: A valid JavaScript file ready for execution.

**Success Indicators**:
- `poc.js` file created without syntax errors
- Code includes require('git-lib') and git.add() call

### Step 2: Verify Clean Environment
procedure: [[procedures/Exploit-git-lib-RCE-via-Command-Injection]]

**Objective**: Ensure no existing 'HACKED' file to confirm successful exploitation later.

**Instructions**: Manually inspect the current directory using `ls` or file explorer to check for the absence of 'HACKED'.

**Expected Output**: No 'HACKED' file present.

**Success Indicators**:
- Filesystem shows no 'HACKED' file

### Step 3: Install Vulnerable Module
procedure: [[procedures/Exploit-git-lib-RCE-via-Command-Injection]]

**Objective**: Install the vulnerable git-lib version 1.6.0 using npm to set up the exploitable environment.

**Instructions**: Run the following command in the terminal:

using [[commands/npm-install-git-lib]]:

```bash
npm i git-lib
```

**Expected Output**: Installation logs confirming git-lib@1.6.0 added to node_modules.

**Success Indicators**:
- node_modules/git-lib directory exists
- package.json updated with dependency

### Step 4: Initialize Git Repository
procedure: [[procedures/Exploit-git-lib-RCE-via-Command-Injection]]

**Objective**: Set up a git repository to prevent conflicts when the module interacts with git operations.

**Instructions**: Execute the git init command in the current directory:

using [[commands/git-init]]:

```bash
git init
```

**Expected Output**: Message like 'Initialized empty Git repository in /path/to/dir/.git/'.

**Success Indicators**:
- .git directory created
- Repository initialized successfully

### Step 5: Execute Proof of Concept
procedure: [[procedures/Exploit-git-lib-RCE-via-Command-Injection]]

**Objective**: Trigger the RCE by running the PoC, which injects and executes the shell command via child_process.exec in git-lib.

**Instructions**: Run the PoC script using Node.js:

using [[commands/node-execute-poc]]:

```bash
node poc.js
```

**Expected Output**: Promise resolution from git.add() and successful command chaining without errors.

**Success Indicators**:
- Script executes without crashing
- No immediate error from git-lib

### Step 6: Verify Exploitation
procedure: [[procedures/Exploit-git-lib-RCE-via-Command-Injection]]

**Objective**: Confirm RCE by checking for the created 'HACKED' file from the injected touch command.

**Instructions**: Re-inspect the filesystem for the 'HACKED' file using `ls`.

**Expected Output**: 'HACKED' file now exists in the directory.

**Success Indicators**:
- 'HACKED' file present, timestamp matching execution time
- File size 0 bytes (from touch command)

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable git-lib module
2. Injection of arbitrary shell command via git.add() leading to file creation
3. Demonstration of full RCE capability on the host OS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]] Unix Shell
- [[Exploitation for Client Execution]] Exploitation for Client Software

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
