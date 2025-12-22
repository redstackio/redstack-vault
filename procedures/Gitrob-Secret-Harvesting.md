---
id: b4f853ce-5e18-42ad-bbc2-3d8dc90232d4
name: Gitrob-Secret-Harvesting
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:00.178891+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
sub_techniques:
  - '[[sub-techniques/Credentials In Files|T1552.001 - Credentials In Files]]'
tags:
  - '[[tags/Git]]'
  - '[[tags/Gitrob]]'
  - '[[tags/Harvesting secrets]]'
  - '[[tags/Insecure Source Code Management]]'
  - '[[tags/Tools]]'
commands:
  - '[[commands/gitrob-install]]'
  - '[[commands/gitrob-run-scan]]'
platforms:
  - Linux
tools:
  - '[[tools/Gitrob]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Gitrob-Secret-Harvesting

## Summary

This procedure uses the Gitrob tool to scan target organization's public and private GitHub repositories for sensitive information such as passwords, API keys, and other secrets, enabling credential harvesting to identify and exploit insecure source code management practices.

## Description

Gitrob is an open-source tool designed to detect hardcoded secrets in GitHub repositories by leveraging GitHub's search functionality and custom regex patterns for common secret types. In an offensive security context, it allows attackers to systematically harvest credentials from exposed code, which can lead to unauthorized access to cloud services, internal systems, or other resources protected by those secrets. Defenders can use it proactively to audit repositories and remediate exposures. The procedure assumes access to a GitHub personal access token with repository read permissions and focuses on scanning organization-owned repositories. Successful execution produces a report of potential secrets with remediation recommendations, mapped to MITRE ATT&CK for unsecured credentials in files.

## Requirements

1. A GitHub personal access token with 'repo' scope for accessing private repositories.
2. Go (Golang) environment installed on the attacker's system (version 1.16+).
3. Network access to GitHub API endpoints.
4. Target organization name or repository list for scanning.

## Defense

Defensive measures and detection strategies:

- Implement secret scanning tools like GitHub's built-in secret scanning or TruffleHog at the repository level.
- Enforce policies prohibiting secrets in code using pre-commit hooks and CI/CD scans.
- Monitor GitHub API access logs for unusual token usage or high-volume searches.
- Rotate credentials immediately upon detection of exposure and revoke compromised tokens.

## Objectives

1. Identify and extract sensitive credentials from public and private GitHub repositories.
2. Generate a report of discovered secrets for further exploitation or remediation.
3. Assess the security posture of the target's source code management practices.

## Instructions

### Step 1: Install Gitrob

**Context**: Install the Gitrob tool using Go to prepare for repository scanning. This step ensures the binary is available on the system.

**Command** ([[commands/gitrob-install]]):
```bash
go install github.com/michenriksen/gitrob@latest
```

> This command downloads and compiles Gitrob from the official repository. Expected output includes successful installation confirmation, with the binary placed in $GOPATH/bin or $HOME/go/bin. Verify installation by running `gitrob --version` to confirm the tool is accessible.

### Step 2: Configure GitHub Access Token

**Context**: Set the required environment variable for GitHub authentication to enable access to private repositories and higher API rate limits.

**Instructions**: Generate a GitHub personal access token via GitHub settings (Developer settings > Personal access tokens > Fine-grained tokens) with 'repo' scope. Then export it:

```bash
export GITROB_ACCESS_TOKEN=ghp_your_token_here
```

> Replace `ghp_your_token_here` with your actual token. This token must have read access to the target organization's repositories. Expected output is no visible response, but subsequent Gitrob runs will authenticate successfully without API rate limit errors.

### Step 3: Run Gitrob Scan on Target Organization

**Context**: Execute the scan against the target organization's repositories to discover secrets. This step performs the core harvesting operation.

**Command** ([[commands/gitrob-run-scan]]):
```bash
gitrob -org target-org-name -output results.json
```

> Replace `target-org-name` with the actual organization (e.g., `example-corp`). The `-org` flag targets all repositories under the organization; use `-repo` for specific repos if needed. Expected output is a JSON report in `results.json` listing discovered secrets, including file paths, commit hashes, and secret types (e.g., AWS keys, passwords). Review the report for high-value findings like API keys. If no secrets are found, the output will indicate an empty results file.

### Step 4: Review and Validate Findings

**Context**: Analyze the scan results to confirm valid secrets and plan next actions, such as testing credentials.

**Instructions**: Open the output file and filter for secrets matching your objectives:

```bash
cat results.json | jq '.findings[] | select(.secret_type == "aws_access_key")'
```

> Use `jq` for JSON parsing if installed. Expected output: Structured data on potential secrets. Validate by testing extracted credentials against target services (e.g., AWS CLI for keys). Success is confirmed by functional access using harvested secrets.
