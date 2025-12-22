---
id: 2f71f98f-c4e8-41a8-8152-8aa6aea41664
name: whoami-display-current-user-sid
type: command
executor: command_prompt
data: whoami /user
output: |-
  C:\>whoami /user

  USER INFORMATION
  ----------------

  User Name SID
  ========= =============================================
  dev\bob   S-1-5-21-1576920733-1301476157-954876328-1108
created_at: '2020-07-20T22:27:56.254490+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - discovery
  - sid
verified: true
validated: true
---

# whoami-display-current-user-sid

## Command

```command_prompt
whoami /user
```

## Description

This command displays the security identifier (SID) of the currently logged-in user, including the domain SID prefix. It is essential for reconnaissance in Active Directory environments to identify domain boundaries and user privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user | Displays user name and SID | Yes |

## Examples

### Basic Usage

```command_prompt
whoami /user
```

### Advanced Usage

Combine with /groups for full privilege info: whoami /user /groups

## Expected Output

```
USER INFORMATION
----------------

User Name SID
========= =============================================
dev\bob   S-1-5-21-1576920733-1301476157-954876328-1108
```

## Related

- [[procedures/Forge-Internal-Forest-Trust-Ticket-and-Escalate-to-Parent-DA-via-SIDHistory]]
- [[commands/wmic-get-group-sid-from-active-directory]]
