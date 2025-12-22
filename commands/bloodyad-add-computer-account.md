---
type: command
executor: bash
data: >-
  python bloodyAD.py -d $_DOMAIN -u $_USERNAME -p $_PASSWORD --host $_DC_IP
  addComputer $_COMPUTER_NAME $_COMPUTER_PASSWORD
output: null
created_at: '2023-04-06T03:56:06.137368+00:00'
updated_at: '2023-04-10T20:36:10.281363+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - account-creation
verified: true
validated: true
---

# bloodyad-add-computer-account

## Command

```bash
python bloodyAD.py -d $_DOMAIN -u $_USERNAME -p $_PASSWORD --host $_DC_IP addComputer $_COMPUTER_NAME $_COMPUTER_PASSWORD
```

## Description

Creates a new computer account in Active Directory using LDAP operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain | Yes |
| $_USERNAME | Username | Yes |
| $_PASSWORD | Password | Yes |
| $_DC_IP | DC IP | Yes |
| $_COMPUTER_NAME | New computer name (e.g., cve) | Yes |
| $_COMPUTER_PASSWORD | Computer account password | Yes |

## Examples

### Basic Usage

```bash
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 addComputer cve 'CVEPassword1234*'
```

## Expected Output

Success message: "Computer account added successfully."

## Related

- [[procedures/Domain-Takeover-via-Certifried-CVE-2022-26923]]
