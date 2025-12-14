---
data: ssh privilege0_user@192.168.1.1 'show version'
tags:
  - ssh
  - verification
type: command
output: null
executor: bash
platforms:
  - Embedded Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.637Z'
id: 5036ad8a-be7b-4a8b-b34a-66cf1b01f5c6
verified: false
validated: true
submitted: true
---
# ssh-execute-basic

## Command

```bash
ssh privilege0_user@192.168.1.1 'show version'
```

## Description

Runs a basic CLI command via SSH to verify privilege-0 access level on the EdgeSwitch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| privilege0_user | Privilege-0 username | Yes |
| 192.168.1.1 | Target IP | Yes |
| 'show version' | Safe CLI command | Yes |

## Examples

### Basic Usage

```bash
ssh privilege0_user@192.168.1.1 'show version'
```

### Advanced Usage

```bash
ssh privilege0_user@192.168.1.1 'show logging'
```

## Expected Output

Device version and firmware details, confirming limited access.

## Related

- [[commands/ssh-authenticate]]
- [[procedures/Authenticate-as-Privilege-0-User-on-Ubiquiti-EdgeSwitch]]
