---
id: f3151831-ef36-4ebd-bc48-0e501bf0617e
type: code
name: wes-ng-systeminfo-and-update
language: bash
verified: true
created_at: '2023-04-06T03:56:28.514350+00:00'
updated_at: '2023-04-10T20:37:50.960310+00:00'
platforms:
  - Windows
tags:
  - exploitation
  - suggester
validated: true
---

# wes-ng-systeminfo-and-update

## Code

```bash
# First obtain systeminfo
systeminfo
systeminfo > systeminfo.txt
# Then feed it to wesng
python3 wes.py --update-wes
python3 wes.py --update
python3 wes.py systeminfo.txt
```

## Description

Script to capture systeminfo, save it, update WES-NG, and run a scan to suggest Windows exploits based on patch levels.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| systeminfo.txt | Output file for systeminfo | custom-systeminfo.txt |

## Usage

Execute sequentially in a shell for automated privesc vuln discovery; useful in scripted red team ops.

## Detection

- systeminfo.exe runs (common but monitor frequency).
- Python wes.py execution (file monitoring).
- Output files with sensitive system details (DLP rules).

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/WES-NG]]
