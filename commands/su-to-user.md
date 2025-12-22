---
type: command
executor: bash
data: su $_USERNAME
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - execution
  - privesc
verified: true
validated: true
---

# su-to-user

## Command

```bash
su $_USERNAME
```

## Description

Switches to another user account, prompting for password if set, to escalate privileges after account creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username | Yes |

## Examples

### Basic Usage

```bash
su hacker
```

### Advanced Usage (with dash for clean env)

```bash
su - dummy
```
Loads user's environment.

## Expected Output

```
Password: 
# whoami
root
```
Prompt changes to # on success.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-passwd]]
- [[commands/add-user-to-etc-passwd-with-hash]]
