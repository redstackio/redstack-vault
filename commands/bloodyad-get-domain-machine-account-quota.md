---
type: command
executor: bash
data: >-
  python bloodyAD.py -d $_DOMAIN -u $_USERNAME -p $_PASSWORD --host $_DC_IP
  getObjectAttributes 'DC=$_DOMAIN' ms-DS-MachineAccountQuota
output: null
created_at: '2023-04-06T03:56:06.137368+00:00'
updated_at: '2023-04-10T20:36:10.281363+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - recon
verified: true
validated: true
---

# bloodyad-get-domain-machine-account-quota

## Command

```bash
python bloodyAD.py -d $_DOMAIN -u $_USERNAME -p $_PASSWORD --host $_DC_IP getObjectAttributes 'DC=$_DOMAIN' ms-DS-MachineAccountQuota
```

## Description

Retrieves the ms-DS-MachineAccountQuota attribute from the Active Directory domain root, indicating how many computer accounts a user can create without admin privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., lab.local) | Yes |
| $_USERNAME | Domain username | Yes |
| $_PASSWORD | User password | Yes |
| $_DC_IP | Domain controller IP | Yes |

## Examples

### Basic Usage

```bash
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 getObjectAttributes 'DC=lab,DC=local' ms-DS-MachineAccountQuota
```

## Expected Output

JSON response with the quota value:

{
  "ms-DS-MachineAccountQuota": ["10"]
}

## Related

- [[procedures/Domain-Takeover-via-Certifried-CVE-2022-26923]]
