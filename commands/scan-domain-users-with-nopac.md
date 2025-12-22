---
id: 05abc538-01b1-4493-8e24-9d7c788e3408
name: scan-domain-users-with-nopac
type: command
executor: bash
data: noPac.exe scan -domain htb.local -user user -pass 'password123'
output: null
created_at: '2023-04-06T03:56:03.185776+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - enumeration
verified: true
validated: true
---

# scan-domain-users-with-nopac

## Command

```bash
noPac.exe scan -domain htb.local -user user -pass 'password123'
```

## Description

This command uses noPac.exe to scan an Active Directory domain for users and potential impersonation targets, authenticating with provided credentials to enumerate without alerting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| scan | Initiates domain scan mode | Yes |
| -domain | Target domain name (e.g., htb.local) | Yes |
| -user | Username for authentication | Yes |
| -pass | Password for the user | Yes |

## Examples

### Basic Usage

```bash
noPac.exe scan -domain example.com -user lowpriv -pass 'Passw0rd!'
```

### Advanced Usage

Scan with additional verbosity if supported by tool.

## Expected Output

List of enumerated users and services, e.g., "Users found: 50, SPNs: 10 including krbtgt and admins."

## Related

- [[procedures/Sam-Account-Name-Spoofing-for-User-Impersonation]]
- [[tools/nopac]]
