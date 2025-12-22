---
id: c33cd784-ed99-4f57-93d9-9261e16f32d9
name: yar-scan-git-repo-for-secrets
type: command
executor: bash
data: yar -o $_ORG_NAME --both
output: null
created_at: '2023-04-06T03:56:00.144387+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - scanning
  - secrets
  - git
  - yar
verified: true
validated: true
---

# yar-scan-git-repo-for-secrets

## Command

```bash
yar -o $_ORG_NAME --both
```

## Description

This command runs Yar to scan the current Git repository (or specified path) for secrets like API keys and passwords. The `-o` flag specifies the organization context for reporting, and `--both` scans both the Git history and uncommitted files for comprehensive detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o $_ORG_NAME` | Organization or repo name for output labeling (e.g., 'acme-corp') | Yes |
| `--both` | Scan both committed history and working directory | No (default is history only) |

## Examples

### Basic Usage

```bash
yar -o acme-corp --both
```

### Advanced Usage

Scan a specific path:

```bash
yar -o acme-corp --both /path/to/repo
```

## Expected Output

If secrets are found:

```
[SECRETS FOUND]
AWS_ACCESS_KEY_ID: AKIA... (file: config.py:23)
API_TOKEN: ghp_... (file: .env:5)
```

If none:

`No secrets found.`

Output is tabular for easy parsing; pipe to file with `> secrets.txt` for logging.

## Related

- [[procedures/Git-Secrets-Harvesting-with-Yar]]
- [[commands/go-install-yar-tool]]
