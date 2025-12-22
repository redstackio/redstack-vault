---
id: 9ad3cba9-b022-49be-aeed-5df6e7cae905
name: gitleaks-scan-public-repository-via-docker
type: command
executor: bash
data: 'docker run --rm zricethezav/gitleaks:latest detect -v -r $_REPO_URL'
output: null
created_at: '2023-04-06T03:56:00.200118+00:00'
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

# gitleaks-scan-public-repository-via-docker

## Command

```bash
docker run --rm zricethezav/gitleaks:latest detect -v -r $_REPO_URL
```

## Description

This command uses Docker to run Gitleaks on a public Git repository URL, detecting hardcoded secrets in the commit history without local cloning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REPO_URL | Public Git repository URL (e.g., https://github.com/zricethezav/gitleaks.git) | Yes |
| --rm | Automatically remove the container after execution | Built-in |
| -v | Enable verbose output for detailed logging | Yes |
| detect | Gitleaks subcommand to perform the scan | Built-in |
| -r | Remote repository flag to specify URL | Yes |

## Examples

### Basic Usage

```bash
docker run --rm zricethezav/gitleaks:latest detect -v -r https://github.com/example/repo.git
```

### Advanced Usage

```bash
docker run --rm zricethezav/gitleaks:latest detect -v -r https://github.com/example/repo.git --report-format json --report-path results.json
```

## Expected Output

If secrets are found:

```
[+] 1 potential secret(s) found

Description: AWS Access Key
File: .env
Line: 1
Commit: abc123...
Secret: ********************
```

No secrets:

`[-] No secrets detected.`

## Related

- [[procedures/Detect-Secrets-in-Git-Repositories-with-Gitleaks]]
- [[tools/Gitleaks]]
