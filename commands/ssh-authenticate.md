---
data: ssh privilege0_user@192.168.1.1
tags:
  - ssh
  - authentication
type: command
output: null
executor: bash
platforms:
  - Embedded Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.647Z'
id: 98173eab-a1b5-4462-a6a9-32a8c9d26b6f
verified: false
validated: true
submitted: true
---
# ssh-authenticate

## Command

```bash
ssh privilege0_user@192.168.1.1
```

## Description

Establishes an SSH connection to the Ubiquiti EdgeSwitch using privilege-0 credentials, prompting for password entry to gain initial access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| privilege0_user | Username with privilege-0 access | Yes |
| 192.168.1.1 | Target device IP address | Yes |

## Examples

### Basic Usage

```bash
ssh privilege0_user@192.168.1.1
```

### Advanced Usage

```bash
ssh -p 22 privilege0_user@192.168.1.1 -o StrictHostKeyChecking=no
```

## Expected Output

Successful connection shows device banner and prompt: "Password:" followed by "EdgeSwitch>" upon entry.

## Related

- [[commands/ssh-execute-arbitrary]]
- [[procedures/Authenticate-as-Privilege-0-User-on-Ubiquiti-EdgeSwitch]]
