---
id: f42fb955-ccf2-4eed-9ac9-3cb43c6b59ef
name: Enumerate-Git-Repository-for-Secrets
type: procedure
verified: true
submitted: false
created_at: '2019-10-16T22:13:26.212152+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials in Files]]'
sub_techniques: []
tags:
  - data-exposure
  - git-secrets
  - credential-access
commands:
  - '[[commands/git-log-with-patches]]'
  - '[[commands/git-reflog-with-patches]]'
  - '[[commands/git-log-all-branches]]'
platforms:
  - Linux
  - macOS
  - Windows
tools: []
validated: true
---

# Enumerate-Git-Repository-for-Secrets

## Summary

This procedure enumerates a Git repository's commit history to uncover sensitive information such as credentials, API keys, or other secrets that may have been committed unintentionally or removed but still linger in the history. It is useful in post-exploitation scenarios where access to a developer's repository reveals hardcoded secrets for further lateral movement or privilege escalation.

## Description

Git repositories frequently contain sensitive data due to developers committing configuration files, passwords, or tokens without realizing it. Even if files are deleted or commits are reset, the history persists unless explicitly garbage-collected. This procedure systematically reviews commit messages, file changes (diffs), and reflog entries to identify such secrets. It targets local or remote repositories accessible via Git, assuming the attacker has cloned or has read access. Expected outcomes include extraction of plaintext credentials or hashes that can be used for subsequent attacks like account compromise.

## Requirements

1. Git installed on the attacker's machine (version 2.0 or higher).
2. Access to the target Git repository (local clone or remote URL with read permissions).
3. Bash shell environment for command execution.
4. Basic knowledge of Git concepts like commits and reflog.

## Defense

Defensive measures and detection strategies:

- Implement pre-commit hooks and tools like git-secrets or gitleaks to scan for secrets before pushing.
- Enforce .gitignore rules to exclude sensitive files (e.g., .env, config files with credentials).
- Regularly perform git gc --prune=now to remove unreachable objects, though this doesn't affect cloned repos.
- Monitor repository access logs for unauthorized clones or pulls.
- Use repository scanning tools in CI/CD pipelines to detect secrets in history.

## Objectives

1. Identify sensitive information in commit messages and file contents.
2. Recover deleted or reset commits containing secrets via reflog.
3. Extract usable credentials for further exploitation.
4. Validate findings by searching outputs for common secret patterns (e.g., AWS keys, passwords).

## Instructions

### Step 1: Enumerate Commit Messages

**Context**: Start by reviewing commit messages across all branches for any incidental leaks of sensitive data, such as mentions of credentials or configurations.

**Command** ([[commands/git-log-all-branches]]):
```bash
git log --all
```

> This command lists commits from all branches, showing author, date, and message. Scan the output for keywords like 'password', 'key', or 'secret'. If a message reveals useful info, note the commit hash for deeper inspection.

### Step 2: Review Commit History with File Changes

**Context**: Examine the full diff of changes in each commit to uncover secrets in added, modified, or deleted files, such as hardcoded credentials in source code or configs.

**Command** ([[commands/git-log-with-patches]]):
```bash
git log -p
```

> The -p flag shows patch diffs for each commit. Look for lines with credentials (e.g., 'password=secret') in files like .env or application configs. Pipe to grep for efficiency: git log -p | grep -i password.

### Step 3: Check Reflog for Lost Commits

**Context**: Use reflog to access hidden or reset commits that might contain secrets removed from the main history, providing a broader view of repository changes.

**Command** ([[commands/git-reflog-with-patches]]):
```bash
git reflog -p
```

> This reveals the reflog with patches, including stashed or reset changes. Search for secret patterns in the output. Success is indicated by discovering commits not visible in standard log.
