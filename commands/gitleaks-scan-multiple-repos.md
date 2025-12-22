---
id: cb742ede-8b54-41da-95fa-2866b92c5330
name: gitleaks-scan-multiple-repos
type: command
executor: bash
data: |
  gitleaks detect --source $_DIRECTORY_PATH --report $_REPORT_PATH --verbose
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

# gitleaks-scan-multiple-repos

## Command

```bash
gitleaks detect --source $_DIRECTORY_PATH --report $_REPORT_PATH --verbose
```

## Description

This command uses Gitleaks to scan all Git repositories within a specified directory for secrets. It recursively detects and analyzes multiple repos, useful for workspace or organization-wide audits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DIRECTORY_PATH | Path to the directory containing multiple Git repos | Yes |
| $_REPORT_PATH | Path for the aggregated JSON report file | No (defaults to stdout) |
| --verbose | Enable detailed output for each repo scanned | No |
| detect | Subcommand to initiate the scan | Yes |
| --source | Path to the directory of repos | Yes |
| --report | Output file for all findings | No |

## Examples

### Basic Usage

```bash
gitleaks detect --source ~/workspaces --report all-secrets.json --verbose
```

### Advanced Usage

```bash
gitleaks detect --source ~/workspaces --report all-secrets.json --verbose --no-git-history
```

> `--no-git-history` skips full history scan for faster execution on large dirs.

## Expected Output

Console output per repo:
```
Scanning repo: /path/to/repo1
[+] FOUND LEAK in repo1
...
Scanning repo: /path/to/repo2
No leaks found.
```

Aggregated report (all-secrets.json):
```json
{
  "secrets": [
    {
      "Description": "API Key",
      "Repo": "repo1",
      "File": "config.py",
      "Secret": "****",
      "Commit": "def456"
    }
  ]
}
```

## Related

- [[procedures/Scan-Local-Git-Repo-for-Secrets-with-Gitleaks]]
- [[tools/Gitleaks]]
