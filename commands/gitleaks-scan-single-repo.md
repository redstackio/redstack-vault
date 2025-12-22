---
id: dbff43e3-c114-474e-b971-cd9b39551672
name: gitleaks-scan-single-repo
type: command
executor: bash
data: |
  gitleaks detect --source $_REPO_PATH --report $_REPORT_PATH --verbose
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - secrets-scanning
  - gitleaks
verified: true
validated: true
---

# gitleaks-scan-single-repo

## Command

```bash
gitleaks detect --source $_REPO_PATH --report $_REPORT_PATH --verbose
```

## Description

This command runs Gitleaks to scan a single local Git repository for hardcoded secrets like API keys and passwords. It examines the full Git history and outputs findings to a report file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_REPO_PATH | Path to the local Git repository directory | Yes |
| $_REPORT_PATH | Path for the output JSON report file (e.g., findings.json) | No (defaults to stdout) |
| --verbose | Enable detailed logging during scan | No |
| detect | Subcommand to perform the detection scan | Yes |
| --source | Specifies the source path for scanning | Yes |
| --report | Specifies the report output file | No |

## Examples

### Basic Usage

```bash
gitleaks detect --source ./my-repo --report secrets.json --verbose
```

### Advanced Usage

```bash
gitleaks detect --source ./my-repo --report secrets.json --verbose --redact-log
```

> Adds `--redact-log` to mask secret values in logs for safer output.

## Expected Output

If secrets are found:
```
[+] FOUND LEAK
Secret: AWS_ACCESS_KEY_ID
File: .env
Line: 12
Commit: abc123...
Value: AKIA...
```

Report file (secrets.json):
```json
{
  "secrets": [
    {
      "Description": "AWS Access Key",
      "StartLine": 12,
      "EndLine": 12,
      "Secret": "****",
      "File": ".env",
      "Commit": "abc123"
    }
  ]
}
```

If no secrets: "No leaks found."

## Related

- [[procedures/Scan-Local-Git-Repo-for-Secrets-with-Gitleaks]]
- [[tools/Gitleaks]]
