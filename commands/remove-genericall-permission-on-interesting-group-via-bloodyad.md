---
id: 9b17708c-ea9f-4c18-8c0a-827fe6746b84
name: remove-genericall-permission-on-interesting-group-via-bloodyad
type: command
executor: bash
data: >-
  python bloodyAD.py -U "$_USERNAME" -P "$_PASSWORD" --host $_DC_HOST -d
  $_DOMAIN setGenericAll "$_TARGET_USER" "cn=$_GROUP_NAME,dc=$_DOMAIN" False
output: null
created_at: '2023-04-06T03:56:06.850730+00:00'
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

# remove-genericall-permission-on-interesting-group-via-bloodyad

## Command

```bash
python bloodyAD.py -U "$_USERNAME" -P "$_PASSWORD" --host $_DC_HOST -d $_DOMAIN setGenericAll "$_TARGET_USER" "cn=$_GROUP_NAME,dc=$_DOMAIN" False
```

## Description

This command uses bloodyAD.py to revoke GenericAll permission from a user on an Active Directory group, adding the False flag to the setGenericAll action. Use for cleanup after testing or to reduce footprint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Username for authentication | Yes |
| -P | Password for authentication | Yes |
| --host | Domain controller hostname or IP | Yes |
| -d | Domain name (e.g., corp.local) | Yes |
| setGenericAll | Action to modify full control | Yes |
| $_TARGET_USER | User to revoke permission from (e.g., devil_user1) | Yes |
| cn=$_GROUP_NAME,dc=$_DOMAIN | Distinguished Name (DN) of the target group | Yes |
| False | Flag to remove the permission | Yes |

## Examples

### Basic Usage

```bash
python bloodyAD.py -U "devil_user1" -P "P@ssword123" --host my.dc.corp -d corp setGenericAll "devil_user1" "cn=INTERESTING_GROUP,dc=corp" False
```

### Advanced Usage

```bash
python bloodyAD.py -U admin -P pass --host dc01.corp -d corp.local setGenericAll "attacker" "cn=Domain Admins,dc=corp,dc=local" False
```

## Expected Output

GenericAll permission removed successfully for devil_user1 on cn=INTERESTING_GROUP,dc=corp.

If the permission doesn't exist: No action taken or error on non-existent ACE.

## Related

- [[procedures/Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]
- [[commands/set-genericall-permission-on-interesting-group-via-bloodyad]]
