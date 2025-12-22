---
id: d1a92bc6-09a4-4549-90e3-1f891edcd911
name: run-trufflehog-scan-on-repository
type: command
executor: bash
data: truffleHog --regex --entropy=False $_REPO_URL
output: null
created_at: '2023-04-06T03:56:00.111745+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - scanning
  - secrets
  - trufflehog
verified: true
validated: true
---

# run-trufflehog-scan-on-repository

## Command

```bash
truffleHog --regex --entropy=False $_REPO_URL
```

## Description

This command scans a Git repository for secrets using regex patterns on commit history. It targets hardcoded credentials like API keys and passwords, ideal for harvesting unsecured data from public or cloned repos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--regex` | Enable regex-based secret detection | Yes |
| `--entropy=False` | Disable entropy analysis to focus on known patterns | Yes |
| `$_REPO_URL` | URL of the Git repository to scan (e.g., https://github.com/user/repo.git) | Yes |

## Examples

### Basic Usage

```bash
truffleHog --regex --entropy=False https://github.com/example/repo.git
```

### Advanced Usage

```bash
truffleHog --regex --entropy=False --json ./local-repo/  # Scan local directory with JSON output
```

## Expected Output

If secrets are found:
```
Secret found: API_KEY in .env at commit def456: sk_live_12345example
Date: 2023-01-01
Repository: example/repo
```
If clean: "No secrets detected." Errors may include network issues or invalid URL.

## Related

- [[commands/install-trufflehog-via-pip]]
- [[procedures/Git-Repository-Secrets-Harvesting-with-TruffleHog]]
