---
type: command
executor: cmd
data: net group "Domain Admins" $_USERNAME /add /domain
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - domain-privilege-escalation
verified: true
validated: true
---

# net-group-add-to-domain-admins

## Command

```cmd
net group "Domain Admins" $_USERNAME /add /domain
```

## Description

Adds a user to the Domain Admins group in an Active Directory domain, providing domain-wide administrative control.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The domain username to add | Yes |
| /add | Adds the user to the group | Built-in |
| /domain | Specifies domain context | Built-in |

## Examples

### Basic Usage

```cmd
net group "Domain Admins" hacker /add /domain
```

## Expected Output

The command completed successfully.

Error if insufficient privileges: "Access is denied."

## Related

- [[procedures/windows-credential-enumeration]]
- [[commands/net-user-list-all-domain-users]]
