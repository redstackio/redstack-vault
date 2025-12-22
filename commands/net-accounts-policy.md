---
id: 6b77f186-3dd2-4e7b-9f43-b5f2f7fa6c53
name: net-accounts-policy
type: command
executor: cmd
data: net accounts
output: null
created_at: '2023-04-06T03:56:28.626680+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - enumeration
  - policy
verified: true
validated: true
---

# net-accounts-policy

## Command

```cmd
net accounts
```

## Description

Displays the current account lockout and password policy settings for the system.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Shows policy info | Yes |

## Examples

### Basic Usage

```cmd
net accounts
```

## Expected Output

```
Computer role: WORKSTATION

Maximum password age: 42 days
Minimum password age: 0 days
Minimum password length: 0 characters
Length of password history maintained: 0 passwords
Lockout threshold: Never
Lockout duration: 30 minutes
Lockout observation window: 30 minutes
Computer role: WORKSTATION
```

Weak settings (e.g., no min length) suggest brute-force potential.

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
