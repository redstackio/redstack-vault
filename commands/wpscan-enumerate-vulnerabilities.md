---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: 'wpscan --url https://www.uberxgermany.com --enumerate vp'
tags:
  - scanning
  - wordpress
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:49.756Z'
verified: false
validated: true
submitted: true
---
# wpscan-enumerate-vulnerabilities

## Command

```bash
wpscan --url https://www.uberxgermany.com --enumerate vp
```

## Description

This command scans a WordPress site for vulnerable plugins (vp) and reports known issues like CSRF and XSS in outdated components.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Target WordPress URL | Yes |
| `--enumerate vp` | Enumerate vulnerable plugins | No |
| `--api-token` | WPScan API token for full DB access | No |

## Examples

### Basic Usage

```bash
wpscan --url https://example.com --enumerate vp
```

### Advanced Usage

```bash
wpscan --url https://example.com --enumerate vp,vt --api-token TOKEN --output vuln_report.json
```

## Expected Output

A console report with sections like 'Vulnerable plugins detected:' listing names, versions, and vulnerabilities (e.g., 'Plugin X: CSRF (High Severity)') followed by URLs and references.

## Related

- [[Related Procedure: Scan-WordPress-Site-for-Vulnerabilities-Using-WPScan]]
