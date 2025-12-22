---
type: command
executor: bash
data: lxc init alpine-priv-esc priv-esc-container -c security.privileged=true
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - lxc
  - privileged-container
verified: true
validated: true
---

# Init-LXC-Container-Privileged

## Command

```bash
lxc init alpine-priv-esc priv-esc-container -c security.privileged=true
```

## Description

Initializes a new LXC/LXD container from the specified image in privileged mode, disabling security restrictions for host access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| alpine-priv-esc | Image alias | Yes |
| priv-esc-container | Container name | Yes |
| -c security.privileged=true | Config to enable privileged mode | Yes |

## Examples

### Basic Usage

```bash
lxc init myimage mycont -c security.privileged=true
```

## Expected Output

Creating mycontainer

Container initialized successfully.

## Related

- [[procedures/Linux-Privilege-Escalation-via-LXC-LXD-Alpine-Image]]
