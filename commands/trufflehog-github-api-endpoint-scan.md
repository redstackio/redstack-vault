---
id: b891a8ee-5ab3-473a-ba14-dc5ed3bbe477
name: trufflehog-github-api-endpoint-scan
type: command
executor: bash
data: >-
  trufflehog github --endpoint=https://api.github.com --org=organization-name
  --token=GITHUB_TOKEN --debug --concurrency=2
output: null
created_at: '2023-04-06T03:55:51.007202+00:00'
updated_at: '2023-04-10T20:21:07.107069+00:00'
platforms:
  - Linux
  - macOS
tags:
  - secrets-scanning
  - github
verified: true
validated: true
---

# trufflehog-github-api-endpoint-scan

## Command

```bash
trufflehog github --endpoint=https://api.github.com --org=organization-name --token=GITHUB_TOKEN --debug --concurrency=2
```

## Description

Performs a customized scan of a GitHub organization via the API, with debugging and concurrency controls for efficient large-scale secret detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `github` | GitHub source type | Yes |
| `--endpoint` | GitHub API base URL | Yes |
| `--org` | Organization to scan | Yes |
| `--token` | GitHub personal access token | Yes (for auth) |
| `--debug` | Enable verbose logging | No |
| `--concurrency` | Number of parallel API requests | No |

## Examples

### Basic Authenticated Scan

```bash
trufflehog github --endpoint=https://api.github.com --org=trufflesecurity --token=ghp_abc123
```

### Debug Mode

```bash
trufflehog github --endpoint=https://api.github.com --org=org --token=TOKEN --debug --concurrency=4
```

## Expected Output

Detailed JSON secrets with debug logs:
```
DEBUG: API call to /orgs/org/repos
{"Type":"Password","Decoded":"pass123","Verified":false}
```
Includes API response traces.
