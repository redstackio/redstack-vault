---
id: 84c93e3f-df47-43c1-a871-dfc513ce77a8
name: api-key-leaks-detection-with-trufflehog
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:51.047962+00:00'
updated_at: '2023-05-26T18:54:15.275796+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Private Keys|T1552.004 - Private Keys]]'
tags:
  - '[[tags/API Key Leaks]]'
  - '[[tags/Tools]]'
  - secrets-scanning
  - credential-discovery
commands:
  - '[[commands/trufflehog-github-api-endpoint-scan]]'
  - '[[commands/trufflehog-github-organization-scan]]'
  - '[[commands/trufflehog-github-repository-scan]]'
  - '[[commands/trufflehog-local-git-repository-scan]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/truffleHog]]'
validated: true
---

# api-key-leaks-detection-with-trufflehog

## Summary

This procedure uses TruffleHog to scan Git repositories, including local Git repos, GitHub repositories, organizations, and API endpoints, for leaked secrets such as API keys, passwords, and private keys. It examines the full commit history to identify high-entropy strings or known patterns that match secret formats, helping security teams or attackers discover unsecured credentials for further exploitation.

## Description

TruffleHog is a specialized tool for detecting secrets in version control systems by analyzing git history, file contents, and API-accessible data. In offensive security scenarios, this procedure enables reconnaissance of target codebases to uncover credentials that could grant access to cloud services, APIs, or internal systems. Defensively, it supports auditing repositories to remediate leaks before exploitation. The technique targets unsecured credentials left in code, aligning with MITRE ATT&CK's focus on credential access through exposed private keys and tokens. Scans can be performed locally or remotely via GitHub's API, requiring appropriate access levels.

## Requirements

1. Docker installed for containerized execution (recommended for isolated runs).
2. TruffleHog binary installed (via Go, pip, or brew) for native scans.
3. GitHub personal access token with repo:read permissions for organization or API scans.
4. Network access to GitHub API or the target repository.
5. Basic command-line proficiency and understanding of git history.

## Defense

- Implement secret scanning in CI/CD pipelines using TruffleHog or similar tools to block commits with secrets.
- Use environment variables or secret management services (e.g., AWS Secrets Manager, HashiCorp Vault) instead of hardcoding credentials.
- Enforce repository access controls and rotate exposed keys immediately upon detection.
- Monitor for anomalous API usage from leaked credentials via cloud logging.

## Objectives

1. Identify API keys, passwords, and private keys embedded in repository commit history or files.
2. Assess the scope of exposure across individual repos, organizations, or local clones.
3. Enable remediation or exploitation based on discovered secrets.
4. Verify scan completeness by checking for verified vs. unverified matches.

## Instructions

### Step 1: Scan a Local Git Repository

**Context**: Clone the target repository locally if needed, then use TruffleHog to scan the git history for secrets. This is ideal for offline analysis or when direct API access is unavailable. It detects secrets across all commits, not just the current state.

**Command** ([[commands/trufflehog-local-git-repository-scan]]):
```bash
trufflehog git file:///path/to/local/repo
```

> This command initializes a scan on the local git directory, outputting any detected secrets with their commit details, file paths, and entropy scores. Replace `/path/to/local/repo` with the actual repository path. Run this after cloning with `git clone <repo-url>` to ensure full history is available.

### Step 2: Scan a Specific GitHub Repository

**Context**: For remote scanning without cloning, use the Docker wrapper to query a single GitHub repo. This fetches the history via GitHub's API and scans for secrets, useful for quick targeted checks.

**Command** ([[commands/trufflehog-github-repository-scan]]):
```bash
trufflehog github --repo=https://github.com/owner/repo-name
```

> Execute this to scan the specified repo. It will list secrets found in commits, including the secret value (partially redacted), source, and verification status. Use a GitHub token if rate-limited.

### Step 3: Scan an Entire GitHub Organization

**Context**: To broaden the scope, scan all public (or accessible) repositories in an organization. This helps identify leaks across multiple projects owned by a target entity.

**Command** ([[commands/trufflehog-github-organization-scan]]):
```bash
trufflehog github --org=organization-name
```

> This command iterates over repos in the org, scanning each for secrets. Output includes repo-specific findings. Provide a token for private orgs via `--token=TOKEN`.

### Step 4: Scan via GitHub API Endpoint

**Context**: For advanced control, directly query the GitHub API endpoint with custom concurrency and debugging. This is suitable for large-scale or authenticated scans requiring fine-tuned parameters.

**Command** ([[commands/trufflehog-github-api-endpoint-scan]]):
```bash
trufflehog github --endpoint=https://api.github.com --org=organization-name --token=GITHUB_TOKEN --debug --concurrency=2
```

> Run this for verbose output and parallel processing. The debug flag shows API interactions; adjust concurrency based on token limits. Replace placeholders with actual values.

## Expected Output

Successful scans produce JSON or plaintext output listing detected secrets, such as:
```
{
  "SourceMetadata": {"Data":{"Git":{"RepositoryURL":"https://github.com/owner/repo","Commit":"abc123"}}},
  "SourceType":"Git",
 "Type":"AWS Access Key",
  "Decoded":"AKIAIOSFODNN7EXAMPLE",
  "Verified":true
}
```
Look for high-confidence matches (Verified: true) indicating exploitable secrets. Unverified ones may be false positives.
