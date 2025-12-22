---
id: 67165108-0b68-4752-b7f5-35e60b8e1cfe
name: gitleaks-scan-github-pull-request-via-docker
type: command
executor: bash
data: >-
  docker run --rm -e GITHUB_TOKEN=$_GITHUB_TOKEN zricethezav/gitleaks:latest
  detect --github-pr=$_PR_URL
output: null
created_at: '2023-04-06T03:56:00.200361+00:00'
updated_at: '2023-04-10T20:33:56.272566+00:00'
platforms:
  - Linux
tags:
  - gitleaks
  - secrets
  - github
  - pr
verified: true
validated: true
---

# gitleaks-scan-github-pull-request-via-docker

## Command

```bash
docker run --rm -e GITHUB_TOKEN=$_GITHUB_TOKEN zricethezav/gitleaks:latest detect --github-pr=$_PR_URL
```

## Description

This command scans a specific GitHub pull request for secrets using Docker, authenticating with a token for private access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GITHUB_TOKEN | GitHub personal access token | Yes (for private) |
| $_PR_URL | Pull request URL (e.g., https://github.com/owner/repo/pull/123) | Yes |
| --rm | Auto-remove container | Built-in |
| detect | Perform detection | Built-in |
| --github-pr | Specify PR to scan | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -e GITHUB_TOKEN=ghp_abc123 zricethezav/gitleaks:latest detect --github-pr=https://github.com/zricethezav/gitleaks/pull/1
```

### Advanced Usage

```bash
docker run --rm -e GITHUB_TOKEN=ghp_abc123 zricethezav/gitleaks:latest detect --github-pr=https://github.com/zricethezav/gitleaks/pull/1 --verbose
```

## Expected Output

If secret in PR:

```
Leak detected in PR diff: Token=abc123...
```

No issues:

`Scan complete, no leaks.`

## Related

- [[procedures/Detect-Secrets-in-Git-Repositories-with-Gitleaks]]
- [[tools/Gitleaks]]
