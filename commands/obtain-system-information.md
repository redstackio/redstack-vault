---
id: 2bac0806-bc1f-461f-b205-cd4e35f5e375
name: obtain-system-information
type: command
executor: cmd
data: systeminfo > systeminfo.txt
output: null
created_at: '2023-04-06T03:56:28.514406+00:00'
updated_at: '2023-04-10T20:37:50.966188+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - systeminfo
verified: true
validated: true
---

# obtain-system-information

## Command

```cmd
systeminfo > systeminfo.txt
```

## Description

Captures detailed system configuration, including OS version, patches, and hardware, for input into exploit suggesters like WES-NG.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| > systeminfo.txt | Redirects output to a file for later use | Yes |

## Examples

### Basic Usage

```cmd
systeminfo > systeminfo.txt
```

### Advanced Usage

View on screen first: `systeminfo`

## Expected Output

File with lines like "OS Name: Microsoft Windows Server 2016 Standard", "Hotfix(s): 50 Hotfix(es) installed.", used to identify unpatched vulns.

## Related

- [[procedures/windows-privilege-escalation-using-powerup-privesccheck-and-wes-ng]]
- [[tools/WES-NG]]
