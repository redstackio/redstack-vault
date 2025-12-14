---
id: uuid-placeholder-9012
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.490Z'
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

This command scans a WordPress site for vulnerable plugins and core issues using WPscan, identifying risks like CSRF and XSS from outdated components. Use it during reconnaissance to assess web application security without active exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | The target WordPress site URL | Yes |
| `--enumerate vp` | Enumerate vulnerable plugins (vp); can extend to other modules like u (users) or cb (config backups) | No |

## Examples

### Basic Usage

```bash
wpscan --url https://example.com --enumerate vp
```

### Advanced Usage

```bash
wpscan --url https://example.com --enumerate vp,vt --api-token YOUR_TOKEN
```

> Adds vulnerable themes (vt) and uses WPscan API for detailed vuln info.

## Expected Output

A formatted report showing site info, interesting findings, and a list of vulnerable plugins with CVE details, e.g., 'Vulnerable Plugin: XYZ v1.0 - XSS (CVE-2018-1234)'. Successful run ends with no errors and populated vulnerability sections.

## Related

- [[commands/wpscan-update]]
- [[procedures/Scan-WordPress-Site-for-Vulnerabilities-using-WPscan]]
