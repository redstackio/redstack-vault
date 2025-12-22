---
id: a5e97a97-b4ba-4ad3-881a-5c94bb65d640
name: update-wes-ng
type: command
executor: bash
data: |-
  python3 wes.py --update-wes
  python3 wes.py --update
  python3 wes.py systeminfo.txt
output: null
created_at: '2023-04-06T03:56:28.514461+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - update
  - suggester
verified: true
validated: true
---

# update-wes-ng

## Command

```bash
python3 wes.py --update-wes
python3 wes.py --update
python3 wes.py systeminfo.txt
```

## Description

Updates WES-NG database and runs a scan on systeminfo.txt to suggest exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --update-wes | Updates WES database | Yes |
| --update | Refreshes additional data | Yes |
| systeminfo.txt | Input file for analysis | Yes |

## Examples

### Basic Usage

```bash
python3 wes.py --update-wes && python3 wes.py --update && python3 wes.py systeminfo.txt
```

## Expected Output

Exploit suggestions like "CVE-2017-0144: Applicable - Use MS17-010 PoC".

## Related

- [[tools/WES-NG]]
- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
