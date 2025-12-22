---
id: 6fcd1c1c-61f6-45b5-abf6-977e0bb6b0fc
name: Git-Secrets-Harvesting-with-Yar
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.149950+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Data from Information Repositories]]'
sub_techniques: []
tags:
  - git
  - secrets-harvesting
  - insecure-source-code-management
  - tools
  - yar
commands:
  - '[[commands/go-install-yar-tool]]'
  - '[[commands/yar-scan-git-repo-for-secrets]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/yar]]'
validated: true
---

# Git-Secrets-Harvesting-with-Yar

## Summary

This procedure uses the Yar tool to scan Git repositories for exposed secrets such as passwords, API keys, and other sensitive information. It is particularly useful in red team engagements or security assessments to identify insecure storage of credentials in source code repositories, enabling further exploitation like unauthorized access to services.

## Description

Git repositories often inadvertently contain hardcoded secrets due to developer oversight, posing a significant risk for data breaches. Yar is a lightweight, command-line tool written in Go that automates the detection of these secrets by scanning repository contents against known patterns for common credential types. This procedure outlines the installation and execution of Yar on a target Git repository, assuming the attacker has read access (e.g., via public repos or compromised credentials). It maps to MITRE ATT&CK technique T1213 (Data from Information Repositories) under the Collection tactic, as it involves extracting sensitive data from version control systems. The process is non-intrusive and can be run offline after cloning the repository.

## Requirements

1. Go runtime installed (version 1.16 or later) on the attacker's machine.
2. Read access to the target Git repository (e.g., clone URL or local copy).
3. Basic command-line knowledge for navigation and execution.
4. Network access if cloning from a remote repository.

## Defense

Defensive measures and detection strategies:

- Implement secret scanning in CI/CD pipelines using tools like GitHub Secrets Scanning or TruffleHog to prevent commits of sensitive data.
- Enforce repository access controls and use branch protection rules to limit pushes.
- Monitor for anomalous scans or downloads of repository data using tools like Git audit logs or endpoint detection agents.
- Rotate credentials regularly and use environment variables or secret management services (e.g., AWS Secrets Manager) instead of hardcoding.

## Objectives

1. Identify and extract exposed secrets from Git repositories to assess compromise potential.
2. Evaluate the security posture of source code management practices.
3. Provide actionable findings for remediation, such as secret rotation.

## Instructions

### Step 1: Install Yar Tool

**Context**: Yar must be installed via Go before scanning. This ensures the tool is available for execution. Run this on your attacker's machine with Go installed.

**Command** ([[commands/go-install-yar-tool]]):
```bash
go install github.com/nielsing/yar@latest
```

> This command fetches and compiles Yar from its GitHub repository. Expected output includes download progress and a success message like "go: downloading github.com/nielsing/yar v0.0.0-...". Verify installation by running `yar --help` to see usage options. If Go is not in PATH, ensure `$GOPATH/bin` or `$GOROOT/bin` is added.

### Step 2: Clone or Navigate to Target Git Repository

**Context**: Obtain the repository contents for scanning. If remote, clone it; if local, cd into the directory. This step prepares the environment without triggering alerts if done carefully.

**Command** (using git):
```bash
git clone https://github.com/org/repo.git
cd repo
```

> Replace the URL with the target repository. Expected output: Repository files downloaded locally. If already cloned, simply navigate with `cd /path/to/repo`. Confirm with `ls` to see source files.

### Step 3: Scan Repository for Secrets

**Context**: Execute Yar to analyze the repository for patterns matching known secrets. The `--both` flag scans both committed history and the working directory, providing comprehensive coverage.

**Command** ([[commands/yar-scan-git-repo-for-secrets]]):
```bash
yar -o $_ORG_NAME --both
```

> Substitute `$_ORG_NAME` with the organization or repository identifier (e.g., 'example-org'). Expected output: A list of detected secrets, including type (e.g., AWS key), location (file/line), and the secret value (partially redacted for safety). If no secrets are found, it outputs "No secrets found." Review the output for exploitable items like API tokens.

### Step 4: Verify and Document Findings

**Context**: Validate detected secrets by testing them (e.g., API calls) and log for reporting. This ensures the harvest is actionable.

> Manually test high-value secrets (e.g., curl to an API endpoint). Document matches with file paths and potential impact. If secrets are confirmed, proceed to exploitation in a separate procedure.
