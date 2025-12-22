---
id: 0d552be8-195e-4251-b72a-5046d6aee5a9
name: gitleaks-scan-remote-repo
type: command
executor: bash
data: |
  gitleaks detect --source=https://github.com/zricethezav/gitleaks
output: null
created_at: '2020-07-24T17:11:21.839813+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - gitleaks
  - scanning
  - secrets
verified: true
validated: true
---

# gitleaks-scan-remote-repo

## Command

```bash
gitleaks detect --source=$_REPO_URL
```

## Description

This command scans a remote Git repository for leaked secrets using Gitleaks' detect mode with the --source flag for remote URLs. It is ideal for quick reconnaissance of public repos like those on GitHub to find credentials without local download.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --source or -$_REPO_URL | Full HTTPS URL of the remote Git repo (e.g., https://github.com/user/repo) | Yes |
| --verbose | Enable detailed output during scan | No |
| --report-format=json | Output results in JSON for parsing | No |
| --redact | Redact secret values in output for safety | No |

## Examples

### Basic Usage

```bash
gitleaks detect --source=https://github.com/zricethezav/gitleaks
```

### Advanced Usage

```bash
gitleaks detect --source=https://github.com/zricethezav/gitleaks --report-format json --verbose
```

## Expected Output

If secrets found:

[SEVERITY] Description: Generic Secret found
Rule: generic-api-key
File: README.md:1
Commit: abc123...
Snippet: |api_key: sk-1234567890abcdef|

If no secrets:
No leaks found.

## Related

- [[procedures/Scan-Remote-Git-Repo-for-Sensitive-Information-with-Gitleaks]]
- [[tools/Gitleaks]]
