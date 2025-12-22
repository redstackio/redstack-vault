---
id: 08cda633-3ed1-453a-89d6-e73eeb972321
name: Scan-Local-Git-Repo-for-Secrets-with-Gitleaks
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Credentials in Files]]'
sub_techniques: []
tags:
  - secrets-scanning
  - gitleaks
  - git
  - credentials
  - discovery
commands:
  - '[[commands/gitleaks-scan-single-repo]]'
  - '[[commands/gitleaks-scan-multiple-repos]]'
platforms:
  - Linux
  - macOS
  - Windows
tools:
  - '[[tools/Gitleaks]]'
validated: true
---

# Scan-Local-Git-Repo-for-Secrets-with-Gitleaks

## Summary

This procedure uses Gitleaks, a fast and open-source SAST tool, to scan local Git repositories for hardcoded secrets such as API keys, passwords, tokens, and other sensitive information. It is particularly useful during code audits, red team assessments, or security reviews to identify potential credential exposures in source code histories.

## Description

Gitleaks scans the Git history of repositories to detect patterns matching known secret formats, including private keys, database credentials, and cloud tokens. By examining commits, it uncovers secrets that may have been committed and later removed but still exist in the repository history. This procedure assumes the target repository has been cloned locally and focuses on both single-repo and multi-repo directory scans. It maps to MITRE ATT&CK technique T1552.001 (Credentials In Files) under the Discovery tactic, as it aids in locating unsecured credentials for further exploitation or reporting.

## Requirements

1. Gitleaks tool installed on the system.
2. Local clone of the target Git repository (use `git clone` if not already present).
3. Sufficient disk space and permissions to read the repository directory.
4. Basic command-line access (Bash on Linux/macOS or compatible shell on Windows).

## Defense

Defensive measures include:
- Implementing pre-commit hooks with tools like Gitleaks to block secret commits.
- Using secret scanning in CI/CD pipelines (e.g., GitHub Advanced Security).
- Regularly auditing repository history and rotating exposed credentials.
- Monitoring for anomalous access using exposed secrets via cloud logging (e.g., AWS CloudTrail).

Detection strategies:
- Log Gitleaks executions if run in monitored environments.
- Alert on scans of sensitive repositories using file access monitoring (e.g., Sysmon on Windows).
- Integrate with SIEM for credential exposure events.

## Objectives

1. Identify hardcoded secrets in a single local Git repository.
2. Optionally scan multiple repositories in a directory for broader coverage.
3. Generate a report of findings for remediation or exploitation analysis.
4. Verify no false positives by reviewing matched secrets.

## Instructions

### Step 1: Scan a Single Local Git Repository

**Context**: This step targets one specific repository to detect secrets across its entire Git history, including past commits. Ensure the repository is cloned to a local path before proceeding. This is ideal for focused audits.

**Command** ([[commands/gitleaks-scan-single-repo]]):
```bash
gitleaks detect --source $_REPO_PATH --report $_REPORT_PATH --verbose
```

> The `--source` flag specifies the path to the single repository. `--report` outputs findings to a JSON file for easy parsing. `--verbose` provides detailed output during the scan. Expected output includes a list of detected secrets with file paths, commit hashes, and secret values (redacted in verbose mode for safety). If no secrets are found, it will report "No leaks found."

### Step 2: Scan Multiple Local Git Repositories in a Directory

**Context**: For scanning an entire directory containing multiple Git repositories (e.g., a workspace with several projects), this step automates detection across all repos. Use this when auditing a developer's local workspace or a cloned organization folder. Decision point: If the directory has non-Git folders, Gitleaks will skip them automatically.

**Command** ([[commands/gitleaks-scan-multiple-repos]]):
```bash
gitleaks detect --source $_DIRECTORY_PATH --report $_REPORT_PATH --verbose
```

> The `--source` flag here points to the parent directory, and Gitleaks recursively identifies and scans all Git repos within it. Output mirrors the single-repo scan but aggregates findings from multiple sources. Review the report file for per-repo breakdowns. If scanning large directories, monitor for performance impacts due to Git history traversal.
