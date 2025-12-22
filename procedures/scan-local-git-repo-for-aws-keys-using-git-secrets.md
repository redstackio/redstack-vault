---
type: procedure
description: >-
  Scans a locally cloned Git repository for exposed AWS credentials and other
  secrets using the git-secrets tool.
verified: true
submitted: false
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques:
  - '[[Credentials in Files]]'
tags:
  - aws
  - secrets
  - git
  - credential-access
  - scanning
commands:
  - '[[commands/git-clone-repository]]'
  - '[[commands/git-secrets-scan-current-directory]]'
platforms:
  - Linux
  - macOS
  - Windows
tools:
  - '[[tools/git-secrets]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Scan Local Git Repo for AWS Keys Using Git-Secrets

## Summary

This procedure uses the git-secrets tool to scan a locally cloned Git repository for committed AWS credentials, API keys, passwords, and other sensitive information. It helps identify accidentally exposed secrets in code repositories, which could lead to unauthorized access if exploited. The tool scans against predefined AWS-specific patterns and can be extended with custom scans.

## Description

Git repositories often contain sensitive data like AWS access keys, secret keys, or passwords committed by mistake. The git-secrets tool, developed by AWS Labs, prevents such commits by scanning for known patterns of secrets during git operations like commit and push. In this procedure, we focus on scanning an existing local repository to detect any already committed secrets. This is useful in red team assessments for discovering credentials in leaked or accessible repos, or in defensive audits to clean up repositories. The scan operates on the .git directory and checks historical commits for matches against AWS patterns (e.g., AKIA[0-9A-Z]{16} for access keys). If secrets are found, they are reported with file paths and line numbers for remediation.

## Requirements

1. A locally accessible Git repository (cloned from a target source like GitHub).
2. Git installed on the system.
3. git-secrets tool installed (see [[tools/git-secrets]] for installation).
4. Read access to the repository directory.
5. Bash-compatible shell (Linux/macOS native; Windows via Git Bash).

## Defense

Defensive measures and detection strategies:

- Use git-secrets in pre-commit hooks to prevent secret commits proactively.
- Implement repository scanning in CI/CD pipelines with tools like truffleHog or GitGuardian.
- Monitor for anomalous AWS API activity from discovered keys (e.g., via AWS CloudTrail logs).
- Educate developers on secret management using vaults like AWS Secrets Manager.
- Regularly audit public repositories for exposed credentials using automated scanners.

## Objectives

1. Identify any committed AWS access keys, secret keys, or session tokens in the Git history.
2. Locate the exact files and lines where secrets appear for targeted removal.
3. Verify the repository is clean or document findings for further exploitation/remediation.
4. Expected outcome: A report of matched secrets or confirmation of no secrets found.

## Instructions

### Step 1: Clone the Target Repository

**Context**: If the repository is not already cloned locally, obtain a copy using Git to enable scanning. This step ensures you have the full history for comprehensive scanning.

**Command** ([[commands/git-clone-repository]]):
```bash
git clone $_REPO_URL $_TARGET_DIR
```

> This command fetches the entire repository history to the specified directory. Replace $_REPO_URL with the GitHub or Git repo URL (e.g., https://github.com/user/repo.git) and $_TARGET_DIR with the local path (e.g., ./target-repo). Expected output includes progress messages like "Cloning into 'target-repo'..." and ends with "done." Verify by checking that a .git folder exists in $_TARGET_DIR.

### Step 2: Navigate to the Repository Directory

**Context**: Change into the cloned directory to ensure the scan targets the correct Git repository. Git-secrets relies on the presence of the .git folder in the current working directory.

**Instructions**: Use standard shell navigation.
```bash
cd $_TARGET_DIR
```

> Run this from the parent directory after cloning. Expected output: No output if successful; your prompt changes to reflect the new path (e.g., /path/to/target-repo$). Confirm with `pwd` or `ls -la | grep .git` to see the .git directory.

### Step 3: Scan for Secrets

**Context**: Execute the git-secrets scan to check the repository's Git history for AWS credentials and other patterns. This step performs the core detection, matching against built-in AWS secret patterns.

**Command** ([[commands/git-secrets-scan-current-directory]]):
```bash
git-secrets --scan
```

> This command scans all commits in the current repository. If secrets are found, it outputs details like the secret pattern, file path, commit hash, and line number (e.g., "[AWS Access Key] found in file.py:12"). If no secrets are found, there is no output, indicating a clean repo. For verbose output, consider adding `--scan-history` for deeper historical scans, but `--scan` suffices for basics. Review any output for potential credentials to test or report.

### Step 4: Review and Verify Findings

**Context**: Analyze the scan results to confirm validity and take next actions, such as testing extracted keys or cleaning the repo.

**Instructions**: Pipe output to a file for review if needed.
```bash
git-secrets --scan > secrets-report.txt 2>&1
cat secrets-report.txt
```

> This captures any matches for offline review. Expected output: The same as Step 3, saved to file. Manually validate any reported keys (e.g., via AWS CLI `aws sts get-caller-identity`) to check if they are active. If no output, the repo is clean.
