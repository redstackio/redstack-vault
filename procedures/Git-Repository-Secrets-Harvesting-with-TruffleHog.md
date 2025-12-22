---
id: 50659863-ad69-487c-965b-c39067111b6e
name: Git-Repository-Secrets-Harvesting-with-TruffleHog
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.117184+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - >-
    [[techniques/Credentials from Password Stores|T1555 - Credentials from
    Password Stores]]
sub_techniques: []
tags:
  - '[[tags/Git]]'
  - '[[tags/Harvesting secrets]]'
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Tools]]'
  - '[[tags/trufflehog]]'
commands:
  - '[[commands/install-trufflehog-via-pip]]'
  - '[[commands/run-trufflehog-scan-on-repository]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/truffleHog]]'
validated: true
---

# Git-Repository-Secrets-Harvesting-with-TruffleHog

## Summary

This procedure uses the TruffleHog tool to scan a Git repository's commit history for accidentally committed secrets such as API keys, passwords, and tokens. It performs regex-based searches on file contents across all commits, enabling attackers to harvest unsecured credentials for further exploitation or defenders to identify and remediate leaks.

## Description

Git repositories frequently contain sensitive information due to developer oversights, such as hardcoded credentials in source code or configuration files. TruffleHog automates the detection of these secrets by analyzing the entire Git history, including deleted or modified files, using predefined regular expressions for common secret patterns (e.g., AWS keys, JWT tokens). This technique is particularly effective against public repositories like those on GitHub, where attackers can clone and scan without authentication. In an attack scenario, this could lead to credential access for cloud services, internal systems, or API endpoints. Defenders can use it proactively to audit repositories. The procedure assumes access to the repository URL and focuses on offline scanning after cloning, though direct URL scanning is supported.

## Requirements

1. Network access to the Git repository URL (public or authenticated clone access).
2. Python 3.x environment with pip installed.
3. Installed TruffleHog tool (see [[tools/truffleHog]] for details).
4. Sufficient disk space for cloning large repositories if performing local scans.

## Defense

- Implement pre-commit hooks and CI/CD pipelines to scan for secrets before pushing code (e.g., using TruffleHog in GitHub Actions).
- Use secret management tools like AWS Secrets Manager or HashiCorp Vault to avoid hardcoding credentials.
- Enforce repository access controls and regularly rotate exposed secrets.
- Monitor for anomalous API usage or logins from harvested credentials.

## Objectives

1. Identify and extract sensitive credentials from a Git repository's history.
2. Verify the presence of high-value secrets like API keys or passwords.
3. Remediate or exploit discovered secrets to achieve persistence or lateral movement.

## Instructions

### Step 1: Install TruffleHog

**Context**: Ensure the TruffleHog tool is installed via pip to enable secret scanning capabilities. This step sets up the environment for subsequent repository analysis.

**Command** ([[commands/install-trufflehog-via-pip]]):
```bash
pip install truffleHog
```

> This command installs the TruffleHog package from PyPI. Verify installation by running `truffleHog --version`, which should output the tool's version number without errors.

### Step 2: Scan the Git Repository for Secrets

**Context**: Execute the scan on the target repository to search commit history for matching secret patterns. Use regex mode for precise detection and disable entropy to focus on known formats.

**Command** ([[commands/run-trufflehog-scan-on-repository]]):
```bash
truffleHog --regex --entropy=False $_REPO_URL
```

> Replace $_REPO_URL with the target Git repository URL (e.g., https://github.com/example/repo.git). The command clones the repo if needed and scans all commits. If no secrets are found, it outputs a message indicating a clean scan; otherwise, it lists detected secrets with file paths, commit hashes, and the secret string itself.

### Step 3: Review and Validate Output

**Context**: Analyze the scan results to confirm valid secrets and assess their potential impact. This step involves manual verification to avoid false positives from regex matches.

**Instructions**: Pipe the output to a file for review: `truffleHog --regex --entropy=False $_REPO_URL > secrets.txt`. Open secrets.txt and cross-reference detected items against known secret formats (e.g., AWS keys start with AKIA). Test extracted credentials if applicable (e.g., via API calls).

> Expected output includes lines like: "Secret found: AWS_ACCESS_KEY_ID in file config.py at commit abc123: AKIAIOSFODNN7EXAMPLE". Success is indicated by zero errors during scan and presence of actionable secrets.
