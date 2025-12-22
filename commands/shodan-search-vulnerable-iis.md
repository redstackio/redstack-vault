---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  shodan search --fields ip_str,port,org "port:80 iis 'Microsoft-IIS'
  vuln:CVE-2015-1635" --limit 10
tags:
  - recon
  - shodan
type: command
output: 'Search results with IPs, ports, and orgs matching the query.'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:32.264Z'
verified: false
validated: true
submitted: true
---
# shodan-search-vulnerable-iis

## Command

```bash
shodan search --fields ip_str,port,org "port:80 iis 'Microsoft-IIS' vuln:CVE-2015-1635" --limit 10
```

## Description

Searches Shodan's database for exposed IIS servers on port 80 tagged with CVE-2015-1635 vulnerability, returning key fields like IP, port, and organization to identify targets like DoD servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--fields` | Specify output fields (e.g., ip_str,port,org) | Yes |
| Query string | Search criteria (e.g., port:80 iis vuln:CVE-2015-1635) | Yes |
| `--limit` | Maximum number of results | No |

## Examples

### Basic Usage

```bash
shodan search "port:80 iis vuln:CVE-2015-1635" --limit 5
```

### Advanced Usage

```bash
shodan search --fields ip_str,port,org,product "port:80 iis vuln:CVE-2015-1635 org:'Department of Defense'" --limit 20
```

## Expected Output

A table or JSON list of matching devices, e.g., IP: 192.0.2.1 | Port: 80 | Org: U.S. Dept of Defense, indicating vulnerable exposures.

## Related

- [[Related Procedure: Discover-Vulnerable-IIS-Servers-with-Shodan]]
