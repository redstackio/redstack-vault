---
data: python3 bypass.py
tags:
  - python
  - exploit
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.288Z'
id: 033407be-9723-42ee-9d4d-ba833f87700a
verified: false
validated: true
submitted: true
---
# execute-nextcloud-2fa-bypass-script

## Command

```bash
python3 bypass.py
```

## Description

This command runs a custom Python script (bypass.py) that automates the Nextcloud 2FA bypass by simulating two login sessions, extracting and swapping the 'oc_sessionPassphrase' cookie, and outputting the modified cookies for browser import to gain unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `bypass.py` | Script file implementing Nextcloud session manipulation | Yes |

## Examples

### Basic Usage

```bash
python3 bypass.py
```

### Advanced Usage

```bash
python3 bypass.py --url https://nextcloud.example.com --user Bypass --pass NextCloudEnforcement
```

(Assumes script accepts CLI args for URL and credentials; modify script accordingly.)

## Expected Output

Printed dictionary of cookies, e.g., {'oc_sessionPassphrase': 'swapped_value', ...}. Import these into browser dev tools to complete the bypass.

## Related

- [[commands/install-python-dependencies-for-bypass-script]]
- [[procedures/Bypass-2FA-via-Session-Cookie-Manipulation]]
