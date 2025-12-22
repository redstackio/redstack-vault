---
id: 05725163-c09c-46ab-88e4-4dfd6bb92297
name: trufflehog-scan-github-repo-entropy-disabled
type: command
executor: bash
data: |
  trufflehog --entropy=false $_REPO_URL
output: null
created_at: '2020-07-24T17:11:22.971703+00:00'
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

# trufflehog-scan-github-repo-entropy-disabled

## Command

```bash
trufflehog --entropy=false $_REPO_URL
```

## Description

This command scans a remote Git repository for sensitive information using TruffleHog, but disables entropy-based detection to focus only on regex-matched patterns for known secret types like API keys and passwords. It reduces false positives in noisy repositories.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --entropy=false | Disables high-entropy string detection, relying on patterns only | No (optional flag) |
| $_REPO_URL | The URL of the Git repository to scan (e.g., https://github.com/user/repo) | Yes |

## Examples

### Basic Usage

```bash
trufflehog --entropy=false https://github.com/dxa4481/truffleHog
```

### Advanced Usage

Combine with JSON output for parsing:

```bash
trufflehog --entropy=false --json $_REPO_URL > secrets.json
```

## Expected Output

Outputs pattern-matched secrets only, e.g.:

```
https://github.com/dxa4481/truffleHog/commit/def456

Private Key: -----BEGIN RSA PRIVATE KEY---- (partial)
File: id_rsa:1
Reason: SSH Private Key
```

No entropy-related findings will appear; empty output indicates no pattern matches.

## Related

- [[procedures/Scan-Remote-Git-Repository-for-Sensitive-Information-Using-TruffleHog]]
- [[tools/truffleHog]]
