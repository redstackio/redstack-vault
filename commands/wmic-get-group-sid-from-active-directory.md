---
id: 69b1f115-2baf-44c1-aae6-f73f54791783
name: wmic-get-group-sid-from-active-directory
type: command
executor: command_prompt
data: 'wmic.exe group where name="$_TARGET_GROUP" get name,sid,domain'
output: |-
  C:\>wmic.exe group where name="Enterprise Admins" get name,sid,domain
  Domain  Name               SID
  TESLA   Enterprise Admins  S-1-5-21-3428605742-3005092657-1212549955-519
created_at: '2023-03-14T05:28:32.527173+00:00'
updated_at: '2023-03-14T06:02:49.008864+00:00'
platforms:
  - Windows
tags:
  - discovery
  - active-directory
verified: true
validated: true
---

# wmic-get-group-sid-from-active-directory

## Command

```command_prompt
wmic.exe group where name="$_TARGET_GROUP" get name,sid,domain
```

## Description

This command queries Windows Management Instrumentation (WMI) to retrieve the SID and domain for a specified Active Directory group. It aids in identifying privileged group SIDs for use in token manipulation or privilege escalation attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_GROUP | Name of the group to query (e.g., "Enterprise Admins") | Yes |
| where name= | WMI filter for the group name | Yes |
| get name,sid,domain | Fields to retrieve: name, SID, and domain | Yes |

## Examples

### Basic Usage

```command_prompt
wmic.exe group where name="Domain Admins" get name,sid,domain
```

### Advanced Usage

Query across domains: wmic /node:$_DC group where name="$_TARGET_GROUP" get name,sid,domain

## Expected Output

```
Domain  Name               SID
TESLA   Enterprise Admins  S-1-5-21-3428605742-3005092657-1212549955-519
```

## Related

- [[procedures/Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory]]
- [[commands/whoami-display-current-user-sid]]
