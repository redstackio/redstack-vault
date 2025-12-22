---
id: 246f820e-8a10-4a08-b9aa-2e8adc824ff1
name: trufflehog-local-git-repository-scan
type: command
executor: bash
data: 'trufflehog git file:///path/to/local/repo'
output: null
created_at: '2023-04-06T03:55:51.002388+00:00'
updated_at: '2023-04-10T20:21:07.107069+00:00'
platforms:
  - Linux
  - macOS
tags:
  - secrets-scanning
  - git
verified: true
validated: true
---

# trufflehog-local-git-repository-scan

## Command

```bash
trufflehog git file:///path/to/local/repo
```

## Description

This command scans a local Git repository's full commit history for leaked secrets like API keys and passwords using TruffleHog's native binary. It analyzes git objects for high-entropy strings matching known secret patterns.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `git` | Specifies Git as the source type | Yes |
| `file:///path/to/local/repo` | Path to the local Git repository directory | Yes |

## Examples

### Basic Usage

```bash
trufflehog git file:///home/user/my-repo
```

### With Output to File

```bash
trufflehog git file:///path/to/local/repo --json > secrets.json
```

## Expected Output

The command outputs detected secrets in JSON format, including type, decoded value, and verification status:
```
{"SourceType":"Git","Type":"AWS Access Key","Decoded":"AKIA...","Verified":true}
```
If no secrets are found, it returns empty output or a summary message.
