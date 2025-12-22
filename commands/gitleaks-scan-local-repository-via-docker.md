---
id: 7c5decbf-b31d-4dd9-90d3-80802e86ee77
name: gitleaks-scan-local-repository-via-docker
type: command
executor: bash
data: >-
  docker run --rm -v $_HOST_PATH:/container/path zricethezav/gitleaks:latest
  detect -v --source=/container/path
output: null
created_at: '2023-04-06T03:56:00.200245+00:00'
updated_at: '2023-04-10T20:33:56.272566+00:00'
platforms:
  - Linux
tags:
  - gitleaks
  - secrets
  - scan
verified: true
validated: true
---

# gitleaks-scan-local-repository-via-docker

## Command

```bash
docker run --rm -v $_HOST_PATH:/container/path zricethezav/gitleaks:latest detect -v --source=/container/path
```

## Description

This command mounts a local Git repository directory into a Gitleaks Docker container to scan for secrets in files and history.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HOST_PATH | Host directory path to mount (e.g., /tmp/myrepo) | Yes |
| /container/path | Container mount point (e.g., /tmp/repo) | Yes |
| --rm | Remove container after run | Built-in |
| -v | Verbose output | Yes |
| detect | Scan subcommand | Built-in |
| --source | Path to repository inside container | Yes |

## Examples

### Basic Usage

```bash
docker run --rm -v /tmp/myrepo:/tmp/repo zricethezav/gitleaks:latest detect -v --source=/tmp/repo
```

### Advanced Usage

```bash
docker run --rm -v /tmp/myrepo:/tmp/repo zricethezav/gitleaks:latest detect -v --source=/tmp/repo --redact-log-file
```

## Expected Output

Secrets detected:

```
[+] Secret found in file config.json at line 5: AWS_SECRET_ACCESS_KEY=...
```

Clean scan:

`No leaks detected.`

## Related

- [[procedures/Detect-Secrets-in-Git-Repositories-with-Gitleaks]]
- [[tools/Gitleaks]]
