---
id: 8225b2e4-5ee1-4a09-bafc-1b86ed75ef8c
name: Detect-Secrets-in-Git-Repositories-with-Gitleaks
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.208419+00:00'
updated_at: '2023-04-10T20:33:56.268516+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques: []
tags:
  - '[[tags/Git]]'
  - '[[tags/Gitleaks]]'
  - '[[tags/Harvesting secrets]]'
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/gitleaks-scan-public-repository-via-docker]]'
  - '[[commands/gitleaks-scan-local-repository-via-docker]]'
  - '[[commands/gitleaks-scan-github-pull-request-via-docker]]'
  - '[[commands/install-gitleaks-via-go-get]]'
platforms:
  - Linux
tools:
  - '[[tools/Gitleaks]]'
validated: true
---

# Detect-Secrets-in-Git-Repositories-with-Gitleaks

## Summary

This procedure uses Gitleaks, an open-source tool, to scan Git repositories for accidentally committed secrets such as API keys, passwords, and tokens. It supports scanning public repositories, local clones, and specific GitHub pull requests, enabling attackers or auditors to harvest credentials for further exploitation in credential access or discovery phases of an engagement.

## Description

Gitleaks performs static analysis on Git repositories by examining commit history and file contents against a predefined set of regex patterns for known secret formats. In an offensive security context, this technique uncovers hardcoded credentials in source code, which can lead to unauthorized access to cloud services, databases, or internal systems. It is particularly effective against insecure source code management practices where developers commit sensitive data without proper scanning. The procedure assumes access to the target repository and focuses on three main scanning modes: public URL-based, local path-based, and GitHub PR-specific. Prerequisites include Docker for containerized execution or Go for native installation. Expected outcomes include a report of detected secrets with file paths, commit hashes, and secret values for validation and exploitation.

## Requirements

1. Docker installed on a Linux system for containerized scans (or Go 1.16+ for native installation).
2. Access to the target Git repository: either a public URL, a locally cloned directory, or a GitHub personal access token for private/PR scans.
3. Basic command-line proficiency and network access if scanning remote repositories.
4. Optional: GitHub token with repo:read permissions for pull request scans.

## Defense

- Implement pre-commit hooks with tools like Gitleaks or GitGuardian to scan changes before pushing.
- Use secret management solutions (e.g., AWS Secrets Manager, HashiCorp Vault) instead of hardcoding credentials.
- Enforce repository access controls, rotate exposed secrets immediately, and monitor for anomalous API usage.
- Enable GitHub Advanced Security or similar CI/CD scanning in development pipelines.

## Objectives

1. Identify hardcoded secrets in Git commit history to enable credential harvesting.
2. Generate actionable reports of potential vulnerabilities for exploitation or remediation.
3. Validate findings by extracting and testing discovered credentials against target services.

## Instructions

1. **Scan a Public Git Repository**

   **Context**: This step scans a publicly accessible Git repository URL for secrets without needing to clone it locally. It is ideal for initial reconnaissance on open-source projects.

   **Command** ([[commands/gitleaks-scan-public-repository-via-docker]]):
   ```bash
   docker run --rm zricethezav/gitleaks:latest detect -v -r https://github.com/zricethezav/gitleaks.git
   ```

   > This command pulls the official Gitleaks Docker image, runs a one-time container, enables verbose output (-v), and specifies the remote repository URL (-r). It analyzes the entire Git history for matches against built-in secret patterns. Run this when you have a suspected public repo URL to quickly check for leaks.

2. **Scan a Local Git Repository**

   **Context**: For repositories already cloned locally, this step mounts the directory into the Docker container to perform an in-depth scan. Use this after cloning a target repo during an engagement to avoid network dependencies.

   **Command** ([[commands/gitleaks-scan-local-repository-via-docker]]):
   ```bash
   docker run --rm -v /path/to/local/repo:/path/in/container zricethezav/gitleaks:latest detect -v --source=/path/in/container
   ```

   > Replace /path/to/local/repo with the host directory (e.g., /tmp/myrepo) and /path/in/container with the container mount point (e.g., /tmp/repo). The --source flag points to the mounted path inside the container. This scans the local Git history and files, reporting any secrets found with context like commit SHA and line numbers.

3. **Scan a Specific GitHub Pull Request**

   **Context**: This targets a specific pull request on GitHub, useful for reviewing changes in merge requests where secrets might be introduced. Requires a GitHub token for authentication if the PR is private.

   **Command** ([[commands/gitleaks-scan-github-pull-request-via-docker]]):
   ```bash
   docker run --rm -e GITHUB_TOKEN=your_github_token zricethezav/gitleaks:latest detect --github-pr=https://github.com/owner/repo/pull/123
   ```

   > Set the GITHUB_TOKEN environment variable with a valid token. The --github-pr flag specifies the PR URL. This fetches and scans only the diff of the PR, highlighting new secrets. If no token is needed for public PRs, omit -e GITHUB_TOKEN.

4. **Install Gitleaks Natively (Alternative to Docker)**

   **Context**: If Docker is unavailable, install Gitleaks via Go for repeated use or integration into scripts. This step sets up the binary for direct execution without containers.

   **Command** ([[commands/install-gitleaks-via-go-get]]):
   ```bash
   go install github.com/gitleaks/gitleaks/v8@latest
   ```

   > Ensure $GOPATH/bin is in your PATH. After installation, run `gitleaks version` to verify. This enables native scans like `gitleaks detect -v -r <url>` without Docker overhead.
