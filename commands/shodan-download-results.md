---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  shodan download --limit 100 vulnerable_iis.json "port:80 iis
  vuln:CVE-2015-1635 org:'Department of Defense'"
tags:
  - recon
  - shodan
type: command
output: JSON file downloaded with search results.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:32.231Z'
verified: false
validated: true
submitted: true
---
# shodan-download-results

## Command

```bash
shodan download --limit 100 vulnerable_iis.json "port:80 iis vuln:CVE-2015-1635 org:'Department of Defense'"
```

## Description

Downloads Shodan search results to a JSON file for offline analysis of vulnerable IIS servers, filtering by CVE and organization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--limit` | Number of results to download | No |
| Output file | Filename for JSON export | Yes |
| Query string | Search filter (e.g., port:80 iis vuln:CVE-2015-1635) | Yes |

## Examples

### Basic Usage

```bash
shodan download iis_vulns.json "iis vuln:CVE-2015-1635"
```

### Advanced Usage

```bash
shodan download --limit 50 --fields ip_str,port dod_iis.json "org:'Department of Defense' iis"
```

## Expected Output

File created: vulnerable_iis.json, containing array of device objects with IPs, banners, and vuln details.

## Related

- [[Related Procedure: Discover-Vulnerable-IIS-Servers-with-Shodan]]
