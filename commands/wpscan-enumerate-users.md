---
id: cmd-wpscan-enum-u
data: 'wpscan --url https://nextcloud.com --enumerate u'
tags:
  - recon
  - wordpress
type: command
output: 'Interesting Finding: Valid username: frank'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.644Z'
verified: false
validated: true
submitted: true
---
# wpscan-enumerate-users

## Command

```bash
wpscan --url https://nextcloud.com --enumerate u
```

## Description

This command uses WPScan to enumerate valid usernames on a WordPress site's admin login by detecting response differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Target WordPress URL | Yes |
| `--enumerate u` | Enable user enumeration | Yes |

## Examples

### Basic Usage

```bash
wpscan --url https://example.com --enumerate u
```

### Advanced Usage

```bash
wpscan --url https://example.com --enumerate u -v --api-token YOUR_TOKEN
```

## Expected Output

List of valid usernames, e.g., "[+] Valid username: frank".

## Related

- [[Related Procedure: Enumerate-WordPress-Usernames-with-WPScan]]
