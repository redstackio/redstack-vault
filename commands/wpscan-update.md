---
id: uuid-placeholder-3456
data: wpscan --update
tags:
  - maintenance
  - wordpress
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.477Z'
verified: false
validated: true
submitted: true
---
# wpscan-update

## Command

```bash
wpscan --update
```

## Description

This command updates the WPscan vulnerability database to ensure scans use the latest known issues, essential before running vulnerability enumerations on WordPress sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--update` | Fetches and applies the latest vulnerability data from WPscan repositories | Yes |

## Examples

### Basic Usage

```bash
wpscan --update
```

### Advanced Usage

No advanced flags needed; run periodically.

## Expected Output

Console output confirming the update, e.g., 'Database updated successfully. New vulnerabilities: 50'. Errors if network issues or outdated Ruby.

## Related

- [[commands/wpscan-enumerate-vulnerabilities]]
- [[procedures/Scan-WordPress-Site-for-Vulnerabilities-using-WPscan]]
