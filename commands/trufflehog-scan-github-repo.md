---
id: 9a5ac9ab-2fcd-401b-8172-d51bb2ef56dc
name: trufflehog-scan-github-repo
type: command
executor: bash
data: |
  trufflehog $_REPO_URL
output: null
created_at: '2020-07-24T17:11:22.971519+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - secrets-scanning
verified: true
validated: true
---

# trufflehog-scan-github-repo

## Command

```bash
trufflehog $_REPO_URL
```

## Description

This command scans a remote Git repository (e.g., GitHub) for sensitive information using TruffleHog's default configuration, which includes regex patterns for common secrets and entropy analysis for random strings. Use it during reconnaissance to uncover leaked credentials in public repos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REPO_URL | The URL of the Git repository to scan (e.g., https://github.com/user/repo) | Yes |

## Examples

### Basic Usage

```bash
trufflehog https://github.com/dxa4481/truffleHog
```

### Advanced Usage

Scan with additional output formatting (if supported in TruffleHog version):

```bash
trufflehog --json $_REPO_URL > secrets.json
```

## Expected Output

The command outputs detected secrets in a formatted list, such as:

```
https://github.com/dxa4481/truffleHog/commit/abc123

AWS Key: AKIAIOSFODNN7EXAMPLE (partial)
File: config.py:15
Reason: AWS Access Key
Entropy: 4.2
```

Success is indicated by any listed secrets; no output means no detections.

## Related

- [[procedures/Scan-Remote-Git-Repository-for-Sensitive-Information-Using-TruffleHog]]
- [[tools/truffleHog]]
