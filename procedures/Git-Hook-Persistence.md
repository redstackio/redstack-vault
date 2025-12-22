---
id: cb713ba5-3e7b-4e7a-867d-e0c186646b74
name: Git-Hook-Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:18.377786+00:00'
updated_at: '2023-04-10T20:34:17.900959+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Hijack Execution Flow|T1574 - Hijack Execution Flow]]'
  - '[[techniques/Modify Existing Service|T1031 - Modify Existing Service]]'
sub_techniques: []
tags:
  - '[[tags/Backdooring Git]]'
  - '[[tags/Git Hooks]]'
  - '[[tags/Linux - Persistence]]'
commands:
  - '[[commands/git-config-set-global-hooks-path]]'
  - '[[commands/view-user-git-config]]'
platforms:
  - Linux
tools: []
validated: true
---

# Git-Hook-Persistence

## Summary

Git Hooks are scripts that run automatically when certain actions occur in Git, such as committing or pushing code. By customizing the Git Hooks path via the core.hooksPath configuration variable to point to a directory controlled by the attacker, persistence can be established on a Linux system. This allows arbitrary code execution or data exfiltration whenever the user interacts with Git repositories, such as during commits or pushes, without altering the standard Git installation.

## Description

This procedure targets the Git configuration to hijack the execution flow of hook scripts, which are event-driven scripts in Git (e.g., pre-commit, post-commit). By setting core.hooksPath globally, all Git operations across repositories will look for hooks in the specified attacker-controlled directory instead of the default .git/hooks per repository. This is particularly effective in development environments where developers frequently use Git. The technique requires user-level access to modify the ~/.gitconfig file and assumes the target user has write permissions to a custom directory. Once set, the attacker can place malicious scripts in the hooks directory to achieve persistence, such as logging keystrokes, exfiltrating code, or executing backdoors. This method evades detection as it leverages legitimate Git functionality and does not require root privileges.

## Requirements

1. Access to a Linux system with Git installed (version 1.7+ recommended for hook support).
2. User-level shell access with write permissions to the home directory (~/) to create and modify the Git configuration and hooks directory.
3. Knowledge of common Git workflows on the target to ensure hooks trigger reliably (e.g., the user must commit or push code).

## Defense

Defensive measures and detection strategies:

- Regularly monitor Git Hooks for unauthorized changes by auditing core.hooksPath in ~/.gitconfig and scanning for non-standard hook directories.
- Restrict access to Git configuration settings using file permissions (e.g., chmod 600 ~/.gitconfig) and group policies in shared environments.
- Implement file integrity monitoring (FIM) tools like OSSEC or Auditd to detect modifications to Git configuration files and hook scripts.
- Educate users on verifying git config --list output and avoiding global hook customizations in untrusted environments.
- Use containerized or isolated Git operations to limit persistence impact.

## Objectives

1. Maintain persistence on a Linux system by hijacking Git hook execution.
2. Execute arbitrary code during routine Git operations like commits or pushes.
3. Steal sensitive data, such as source code or credentials, from repositories.

## Instructions

### Step 1: Set Global Hooks Path

**Context**: This step modifies the global Git configuration to redirect hook script execution to an attacker-controlled directory. This ensures that any Git operation triggers scripts from the custom path, enabling persistence. Choose a writable directory in the user's home, such as ~/.git-hooks, to avoid permission issues.

**Command** ([[commands/git-config-set-global-hooks-path]]):
```bash
git config --global core.hooksPath $_HOOKS_DIRECTORY
```

> Run this command to update ~/.gitconfig with the new hooks path. The $_HOOKS_DIRECTORY placeholder should be replaced with a path like ~/.git-hooks. This step succeeds silently if permissions allow; otherwise, it errors with "fatal: unable to access". Why: Redirecting hooks allows placing malicious scripts without modifying per-repo .git directories. Expected output: No stdout on success; verify with the next step.

### Step 2: Create Hooks Directory if Needed

**Context**: Ensure the specified hooks directory exists and is writable. This prepares the environment for placing malicious hook scripts, such as a pre-commit hook that could execute a backdoor.

**Instructions**: Use standard shell commands to create the directory.
```bash
mkdir -p $_HOOKS_DIRECTORY
chmod 755 $_HOOKS_DIRECTORY
```

> Replace $_HOOKS_DIRECTORY with the path set in Step 1 (e.g., ~/.git-hooks). This creates the directory if it doesn't exist and sets appropriate permissions. Why: Git requires the hooks path to exist for script discovery. Expected output: No output on success; use ls $_HOOKS_DIRECTORY to confirm creation.

### Step 3: Verify Git Configuration

**Context**: Confirm the core.hooksPath setting was applied correctly by inspecting the user-level Git config file. This validates the persistence mechanism is in place before adding hooks.

**Command** ([[commands/view-user-git-config]]):
```bash
cat ~/.gitconfig
```

> This displays the entire ~/.gitconfig file. Look for the [core] section containing "hooksPath = $_HOOKS_DIRECTORY". Why: Verification ensures the config change persists across sessions and no errors occurred. Expected output: Sample output showing the updated config:
```
[core]
	hooksPath = /home/user/.git-hooks
``` If the line is missing, rerun Step 1.

### Step 4: Test Hook Execution

**Context**: Place a benign test hook and trigger a Git operation to confirm the custom path is used. This verifies the persistence setup without deploying malicious code.

**Instructions**: Create a simple pre-commit hook script in the custom directory.
```bash
cat > $_HOOKS_DIRECTORY/pre-commit << EOF
#!/bin/bash
echo "Hook executed from custom path" > /tmp/hook-test.log
EOF
chmod +x $_HOOKS_DIRECTORY/pre-commit
```

> Then, in any Git repo, run git commit --allow-empty to trigger the hook. Why: Tests that Git loads hooks from the new path. Expected output: The echo message written to /tmp/hook-test.log, confirming execution. Check with cat /tmp/hook-test.log. If no output, review permissions or config.
