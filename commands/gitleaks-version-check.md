---
id: new-uuid-for-version-check
name: gitleaks-version-check
type: command
executor: bash
data: |
  gitleaks version
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - gitleaks
  - version
verified: true
validated: true
---

# gitleaks-version-check

## Command

```bash
gitleaks version
```

## Description

This command checks the installed version of Gitleaks, ensuring the tool is properly set up before running scans. Use it as a prerequisite verification in reconnaissance procedures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| version   | Displays the current Gitleaks version | Yes (built-in) |

## Examples

### Basic Usage

```bash
gitleaks version
```

### Advanced Usage

Not applicable; this is a simple version query.

## Expected Output

Gitleaks version v8.18.0 (latest release: v8.18.0) (Please see https://github.com/gitleaks/gitleaks/releases/tag/v8.18.0)

## Related

- [[procedures/Scan-Remote-Git-Repo-for-Sensitive-Information-with-Gitleaks]]
- [[commands/gitleaks-scan-remote-repo]]
